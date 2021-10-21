#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Abstract method for other modules."""

import logging
from pathlib import Path
from typing import List, Tuple

LOGFILE = Path("/var/log/interview-bootstrap.log")
logging.basicConfig()
console = logging.StreamHandler()
LOG = logging.getLogger("interview-bootstrap")
LOG.addHandler(console)
LOG.setLevel(logging.INFO)

try:
    logfile = logging.FileHandler(filename=LOGFILE)
    LOG.addHandler(logfile)
except PermissionError:
    pass


class Status:
    """Status."""

    def __init__(self):
        """__init__."""
        self.success = []
        self.error = []  # type: List[Tuple[str, str]]

    def add_success(self, cmd: str, output: str):
        """add_success.

        Args:
            cmd (str): cmd
            output (str): output
        """
        self.success.append((cmd, output))

    def add_error(self, cmd: str, output: str):
        """add_error.

        Args:
            cmd (str): cmd
            output (str): output
        """
        self.error.append((cmd, output))

    @property
    def count(self) -> int:
        """count.

        Args:

        Returns:
            int:
        """
        return sum([len(self.success), len(self.error)])

    @property
    def has_errors(self) -> bool:
        """has_errors.

        Args:

        Returns:
            bool:
        """
        return len(self.error) != 0
