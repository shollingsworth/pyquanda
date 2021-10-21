#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Question data interfaces."""
from typing import Any, Dict, List

from pyquanda.environment import QUESTIONS_DATA
from pyquanda.host.registry import RegistryBase
from pyquanda.exceptions import PreCheckFail
from pyquanda.host.intro import intro_export_b64, intro_load_pickle_b64


class QuestionData:
    """QuestionModule."""

    def __init__(
        self,
        module_name: str,
        intro_b64: str,
        order: int,
        bg_commands: List,
        questions: List = None,
    ):
        """__init__."""
        self.module_name = module_name
        self.order = order
        self.introduction = intro_load_pickle_b64(intro_b64)
        self.questions = questions
        self.question_background_cmds = bg_commands
        QuestionCollection.REGISTRY[module_name] = self

    def get(self) -> Dict[str, Any]:
        """save."""
        nval = {
            "module_name": self.module_name,
            "intro_b64": intro_export_b64(self.introduction),
            "order": self.order,
            "questions": self.questions,
            "bg_commands": self.question_background_cmds,
        }
        no_vals = []
        skip_checks = [
            "bg_commands",
        ]
        for k, v in nval.items():
            if k in skip_checks:
                continue
            if not v:
                no_vals.append(k)
        if no_vals:
            msg = (
                "The following values are missing, please fix ['%s']"
                % "','".join(no_vals)
            )
            raise PreCheckFail(msg)
        return nval


class QuestionCollection(RegistryBase):
    """ModuleQuestions."""

    REGISTRY = {}  # type: Dict[str, QuestionData]
    DATA_SRC = QUESTIONS_DATA

    SRC_CLASS = QuestionData

    @classmethod
    def fetch(cls):
        """fetch."""
        retarr = []
        for obj in sorted(cls.REGISTRY.values(), key=lambda x: x.order):
            retarr.append(obj.get())
        return retarr
