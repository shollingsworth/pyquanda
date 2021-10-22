#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""base classes for hooks module."""

import time
from abc import ABC, abstractmethod
from typing import Dict

from ruamel.yaml.main import YAML

from pyquanda.environment import INTERVIEW_CONFIG_REMOTE_FILE

yaml = YAML()


class Hook(ABC):
    """BaseHookType."""

    @abstractmethod
    def __init__(self, name: str, config: Dict) -> None:
        """__init__.

        Args:
            config (Dict): config

        Returns:
            None:
        """
        self.name = name
        self.vars = yaml.load(INTERVIEW_CONFIG_REMOTE_FILE)  # type: Dict
        if "hooks" in self.vars:
            del self.vars["hooks"]
        self.config = config

    def fmt_json(self, dct: Dict) -> Dict:
        """fmt_json.

        Args:
            dct (Dict): dct

        Returns:
            Dict: response dict
        """
        return {
            "ts": str(time.time()),
            "vars": self.vars,
            "type": self.name,
            "config": self.config,
            "event": dct,
        }

    @abstractmethod
    async def async_send(self, dct: Dict):
        """send.

        Args:
            dct (Dict): dct
        """

    @abstractmethod
    def send(self, dct: Dict):
        """send.

        Args:
            dct (Dict): dct
        """
