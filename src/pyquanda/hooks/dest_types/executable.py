#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Executable type."""

import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Dict
from pyquanda.environment import INTERVIEW_CONFIG_REMOTE_FILE
from pyquanda.hooks.config import DEST_TYPE_EXECUTABLE

from pyquanda.exceptions import PreCheckFail
from pyquanda.hooks import Hook


class ExecutableDest(Hook):
    """ExecutableDest."""

    def __init__(self, name: str, config: Dict) -> None:
        """__init__.

        Args:
            config (Dict): config

        Returns:
            None:

        Raises:
            PreCheckFail: if error
        """
        super().__init__(name, config)
        if not config.get("path"):
            raise PreCheckFail(
                '"path" variable is not set in'
                f" {INTERVIEW_CONFIG_REMOTE_FILE} in the hooks section for"
                f" type {DEST_TYPE_EXECUTABLE}"
            )
        bin_file = Path(config["path"])
        if not bin_file.exists():
            raise PreCheckFail(f"{bin_file} does not exist")
        if not os.access(bin_file, os.X_OK):
            raise PreCheckFail(f"{bin_file} is not executable")
        self.bin = bin_file

    def send(self, dct: Dict):
        with tempfile.TemporaryDirectory() as _tdir:
            tdir = Path(_tdir)
            dfile = tdir.joinpath("out.json")
            out = self.fmt_json(dct)
            dfile.write_text(json.dumps(out))
            cmd = f"{self.bin.absolute()} {dfile}"
            subprocess.call(cmd, shell=True)
