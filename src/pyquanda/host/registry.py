#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Question data interfaces."""
from abc import ABC, abstractmethod
import json
from pathlib import Path
from typing import Any, Dict

from pyquanda.exceptions import PreCheckFail


class DataInterface(ABC):
    """Required Data interface for Registry."""

    @abstractmethod
    def get(self) -> Dict[str, Any]:
        """Return dictionary for export."""


class RegistryBase(ABC):
    """ModuleQuestions."""

    REGISTRY = {}  # type: Dict[str, DataInterface]
    DATA_SRC = Path("")
    SRC_CLASS = type  # type: Any

    @classmethod
    def export(cls):
        """Export data to file."""
        retarr = [i.get() for i in cls.REGISTRY.values()]
        cls.DATA_SRC.write_text(json.dumps(retarr))

    @classmethod
    def add(cls, dct: Dict[str, Any]):
        """add.

        Args:
            dct (Dict): dct
        """
        name = dct["module_name"]  # type: str
        obj = cls.SRC_CLASS(**dct)
        cls.REGISTRY[name] = obj

    @classmethod
    def load(cls):
        """load."""
        if cls.DATA_SRC.exists():
            for dct in json.loads(cls.DATA_SRC.read_text()):
                cls.add(dct)
        else:
            raise PreCheckFail(
                "Error, no questions could be loaded, file"
                f" {cls.DATA_SRC} missing?"
            )

    @classmethod
    def get_module(
        cls, module_name: str
    ):  # pylint: disable=missing-return-type-doc,missing-return-doc
        """get_module.

        Args:
            module_name:
        """
        return cls.REGISTRY[module_name]
