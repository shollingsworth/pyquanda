#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Environment variables, configuration and static filepaths."""
import logging
import tempfile
from pathlib import Path
from typing import Dict, List

from jinja2 import Template

from pyquanda.lib.yaml_util import load_from_bytes, load_from_path

logging.basicConfig()
LOGFILE = Path("/tmp/pyquanda.log")
if not LOGFILE.exists():
    LOGFILE.write_text("")
    LOGFILE.chmod(0o0666)
LOG = logging.getLogger("interview-bootstrap")
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.FileHandler(filename=LOGFILE))

REMOTE_BASE_PATH = Path("/opt/interview_env")
_TMP = Path(tempfile.gettempdir())

HOOK_DIR = REMOTE_BASE_PATH.joinpath("_hooks")
LOCK_FILE = _TMP.joinpath("interview_locfile.lock")
INTERVIEW_CONFIG_REMOTE_FILE = _TMP.joinpath("interview.yaml")
QUESTIONS_DATA = _TMP.joinpath("questions.json")
INTRO_DATA = _TMP.joinpath("intro.json")
INTERVIEW_STATE_REMOTE_FILE = _TMP.joinpath("interview_state.sqlite")


DEMO_DIR = Path(__file__).parent.joinpath("demo")
MOCK_FILE = DEMO_DIR.joinpath("mock_config.yaml")
MOCK_CONFIG = "\n".join(
    MOCK_FILE.read_text().splitlines() + [f"demo_path: {DEMO_DIR}"]
)


class InterviewConfig:
    """InterviewConfig."""

    def __init__(self, mod_path: Path = None):
        """__init__.

        Args:
            mod_path (Path): mod_path
        """
        self.data = load_from_bytes(
            INTERVIEW_CONFIG_REMOTE_FILE.read_bytes()
        )  # type: Dict
        if mod_path is not None:
            comb_vars = dict(self.data)
            var_file = mod_path.joinpath("vars.yaml")
            j2_template = Template(
                mod_path.joinpath("config.yaml").read_text()
            )
            if var_file.exists():
                mod_vars = load_from_path(var_file)
                comb_vars.update(mod_vars)
            self.data = load_from_bytes(j2_template.render(**comb_vars))

    @property
    def username(self) -> str:
        """username.

        Args:

        Returns:
            str:
        """
        return "".join([self.firstname[0], self.lastname])

    @property
    def quanda_id(self) -> str:
        """instance / state id for hooks.

        You may or may not care about this.

        Args:

        Returns:
            str:
        """
        val = self.data.get("quanda_id")
        if not val:
            return "unkown"
        return str(val)

    @property
    def firstname(self) -> str:
        """firstname.

        Args:

        Returns:
            str:
        """
        return self.data["firstname"]

    @property
    def restricted_commands(self) -> List[str]:
        """restricted_commands.

        Args:

        Returns:
            List[str]: list of restricted commands, i.e. bash, zsh, etc shells
            that might be used to breakout
        """
        return self.data.get("shell_settings", {}).get(
            "restricted_commands", []
        )

    @property
    def allow_sudo(self) -> List[str]:
        """allow_sudo.

        Args:

        Returns:
            List[str]: list of allowed sudo commands
        """
        return self.data.get("shell_settings", {}).get("allow_sudo", [])

    @property
    def lastname(self) -> str:
        """lastname.

        Args:

        Returns:
            str:
        """
        return self.data["lastname"]

    @property
    def fqdn(self) -> str:
        """fqdn.

        Args:

        Returns:
            str:
        """
        return self.data["fqdn"]

    def as_dict(self) -> Dict[str, str]:
        """as_dict.

        Args:

        Returns:
            Dict[str, str]: object dict representation
        """
        return {
            i: getattr(self, i)
            for i in dir(self)
            if not any(
                [
                    i.startswith("_"),
                    callable(getattr(self, i)),
                ]
            )
        }
