#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Abstract method for other modules."""
# pylint: skip-file

import sys
from abc import ABC
from logging import Logger
from pathlib import Path
from typing import Any, Dict, Iterator, List, Tuple

from pyquanda.environment import InterviewConfig
from pyquanda.exceptions import PreCheckFail
from pyquanda.environment import LOG
from pyquanda.host.intro import Intro, intro_export_b64
from pyquanda.host.main_intro_data import MainIntroData
from pyquanda.host.question_data import QuestionData
from pyquanda.host.question_state import StateData

ME = sys.modules[__name__]

TYPE_PROBLEM = "problem"
TYPE_SYSTEM = "system"
TYPE_INTRO = "intro"
TYPES = [getattr(ME, i) for i in dir(ME) if i.startswith("TYPE_")]


class BaseModule(ABC):
    """Module interface."""

    def __init__(self, path: Path):
        """initialize class."""
        self.path = path
        vfile = path.joinpath("vars.yaml")
        cfile = path.joinpath("config.yaml")
        self.data_file = cfile
        self.var_file = vfile
        self.data = InterviewConfig(self.path).data

        # Do checks up front to make sure the minimum keys exist
        if not cfile.exists():
            raise PreCheckFail(f"{cfile} does not exist")

        key = "type"
        try:
            self.type = self.data[key]
        except KeyError as _e:
            raise PreCheckFail(f"{cfile} is missing key {key}") from _e

        key = "description"
        try:
            self.description = self.data[key]
        except KeyError as _e:
            raise PreCheckFail(f"{cfile} is missing key {key}") from _e

        key = "order"
        try:
            self.order = int(self.data[key])
        except KeyError as _e:
            raise PreCheckFail(f"{cfile} is missing key {key}") from _e
        except ValueError as _e:
            raise PreCheckFail(
                f"{cfile} key {key} needs to be an integer"
            ) from _e

        self.name = self.path.name
        self.template_path = self.path.joinpath("templates")
        self.state = StateData()
        ModulesCollection.register(self)

    @property
    def log(self) -> Logger:
        """log.

        Args:

        Returns:
            Logger:
        """
        return LOG.getChild(self.name)

    @property
    def network_ports(self) -> List[Dict[str, int]]:
        """network_ports.

        Args:

        Returns:
            List[Dict[str, int]]:
        """
        return self.data.get("network_ports", [])

    @property
    def _introduction(self) -> List[Dict[str, str]]:
        """_introduction.

        Args:

        Returns:
            List[Dict[str, str]]:
        """
        return self.data["introduction"]

    def as_dict(self) -> Dict[str, str]:
        """as_dict.

        Args:

        Returns:
            Dict[str, str]: Dict representing the questions object
        """
        retdict = {}
        for i in dir(self):
            try:
                if i.startswith("_"):
                    continue
                attr = getattr(self, i)
                if isinstance(attr, Path):
                    attr = str(attr.absolute())
                if any(
                    [
                        isinstance(attr, str),
                    ]
                ):
                    retdict[i] = attr
            except AttributeError:
                pass
        dat = dict(self.data)
        dat.update(retdict)
        return dat


class SystemModule(BaseModule):
    def __init__(self, path: Path):
        super().__init__(path)


class QuestionModule(BaseModule):
    def __init__(self, path: Path):
        super().__init__(path)
        self.question_data = QuestionData(
            module_name=self.name,
            intro_b64=intro_export_b64(self.question_intro),
            questions=self.questions,
            order=self.order,
            bg_commands=self.runtime_background_processes,
        )

    @property
    def runtime_background_processes(self) -> List[str]:
        """runtime_background_processes.

        Args:

        Returns:
            List[str]:
        """
        return self.data.get("runtime_background_processes", [])

    @property
    def questions(self) -> List[str]:
        """questions.

        Args:

        Returns:
            List[str]:
        """
        if self.type == TYPE_INTRO:
            return []
        return self.data["questions"]

    def question_export_entry(self) -> Dict[str, Any]:
        """question_export_entry.

        Args:

        Returns:
            Dict[str, Any]: export ready to insert into questions.json
        """
        return {
            "module_name": self.name,
            "intro_b64": intro_export_b64(self.question_intro),
            "questions": self.questions,
            "order": self.order,
            "bg_commands": self.runtime_background_processes,
        }

    @property
    def question_intro(self) -> Intro:
        """question_intro.

        Args:

        Returns:
            Intro:
        """
        intro = Intro(self.description, self.template_path, self.data)
        intro.load(self.data_file, self._introduction)
        return intro


class MainIntroModule(BaseModule):
    def __init__(self, path: Path):
        super().__init__(path)
        self.main_intro_module = MainIntroData(
            module_name=self.name,
            intro_b64=intro_export_b64(self.main_intro),
        )

    @property
    def main_intro(self) -> Intro:
        """question_intro.

        Args:

        Returns:
            Intro:
        """
        intro = Intro(self.description, self.template_path, self.data)
        intro.load(self.data_file, self._introduction)
        return intro

    def main_info_export_entry(self) -> Dict[str, Any]:
        return {
            "module_name": self.name,
            "intro_b64": intro_export_b64(self.main_intro),
        }


class ModulesCollection:
    """Collection of modules."""

    REGISTRY = {
        TYPE_PROBLEM: {},
        TYPE_SYSTEM: {},
        TYPE_INTRO: {},
        "all": {},
    }
    TYPE_LIST = [i for i in REGISTRY if i != "all"]

    @classmethod
    def register(cls, module: BaseModule):
        """register.

        Args:
            module (Module): module

        Raises:
            PreCheckFail: if validation fails
        """
        if module.type not in cls.TYPE_LIST:
            raise PreCheckFail(
                f'module {module.name} if not in "{cls.TYPE_LIST}"'
            )
        cls.REGISTRY[module.type][module.name] = module
        cls.REGISTRY["all"][module.name] = module

    @classmethod
    def all(cls) -> Iterator[BaseModule]:
        """all.

        Args:

        Yields:
            Module: yield all modules
        """
        yield from sorted(
            (i for i in cls.REGISTRY["all"].values()),
            key=lambda x: x.order,
        )

    @classmethod
    def problem_collection(cls) -> Iterator[QuestionModule]:
        """problem_collection.

        Args:

        Yields:
            Module:
        """
        for i in sorted(
            cls.REGISTRY[TYPE_PROBLEM].values(), key=lambda x: x.order
        ):
            yield i

    @classmethod
    def main_intro(cls) -> MainIntroModule:
        """main_intro.

        Args:

        Returns:
            Module: main intro module

        Raises:
            PreCheckFail: if validation fails
        """
        mintro_list = cls.REGISTRY[TYPE_INTRO]
        mintro_len = len(mintro_list)
        if mintro_len != 1:
            raise PreCheckFail(
                "Intro modules collection length is != 1 / given"
                f' {mintro_len}"'
            )
        return mintro_list[0]

    @classmethod
    def system_collection(cls) -> Iterator[SystemModule]:
        """system_collection.

        Args:

        Yields:
            Module:
        """
        for i in sorted(cls.REGISTRY["system"], key=lambda x: x.order):
            yield i

    @classmethod
    def network_ports(cls) -> Iterator[Tuple[str, int]]:
        """network_ports.

        Args:

        Yields:
            Tuple[str, int]
        """
        for i in cls.REGISTRY["all"].values():
            for z in i.network_ports:
                yield z["type"], z["port"]


class ModuleLoader:
    LOAD_MAP = {
        TYPE_INTRO: MainIntroModule,
        TYPE_PROBLEM: QuestionModule,
        TYPE_SYSTEM: SystemModule,
    }

    @classmethod
    def load(cls, path: Path):
        """initialize class."""
        if not path.is_dir():
            return
        # we treat these as hidden / not processed
        if path.name.startswith("_"):
            return
        data = InterviewConfig(path).data
        cls.LOAD_MAP[data["type"]](path)
