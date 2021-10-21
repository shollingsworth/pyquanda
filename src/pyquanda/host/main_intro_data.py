#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Question data interfaces."""
from typing import Any, Dict

from pyquanda.environment import INTRO_DATA
from pyquanda.exceptions import PreCheckFail
from pyquanda.host.registry import RegistryBase
from pyquanda.host.intro import intro_export_b64, intro_load_pickle_b64


class MainIntroData:
    """MainIntroData."""

    def __init__(
        self,
        module_name: str,
        intro_b64: str,
    ):
        """__init__."""
        self.module_name = module_name
        self.introduction = intro_load_pickle_b64(intro_b64)
        MainIntroCollection.REGISTRY[module_name] = self

    def get(self) -> Dict[str, Any]:
        """get.

        Args:

        Returns:
            Dict[str, Any]: dictionary of intro

        Raises:
            PreCheckFail: on error
        """
        nval = {
            "module_name": self.module_name,
            "intro_b64": intro_export_b64(self.introduction),
        }
        no_vals = []
        for k, v in nval.items():
            if not v:
                no_vals.append(k)
        if no_vals:
            msg = (
                "The following values are missing, please fix ['%s']"
                % "','".join(no_vals)
            )
            raise PreCheckFail(msg)
        return nval


class MainIntroCollection(RegistryBase):
    """MainIntroCollection."""

    REGISTRY = {}  # type: Dict[str, MainIntroData]
    DATA_SRC = INTRO_DATA
    SRC_CLASS = MainIntroData
