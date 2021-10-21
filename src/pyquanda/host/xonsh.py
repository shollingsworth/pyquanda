#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XenSH question interface."""
import getpass
import shutil
import socket
import subprocess
import textwrap
from io import TextIOWrapper
from typing import Callable, Dict, List, Optional

import prompt_toolkit.styles.defaults as defstyle
from colors.colors import color
from xonsh.events import events
from xonsh.procs.specs import SubprocSpec

from pyquanda.hooks.config import (
    HOOK_TYPE_QUESTIONABLE,
    HOOK_TYPE_ANSWER,
    HOOK_TYPE_XONSH_COMMAND_ENTERED,
)
from pyquanda.hooks.registry import HookLoader
from pyquanda.hooks.config import EMITTER
from pyquanda.host.nav import NavFooter, Navigation

RESTRICTED = ["bash", "sh", "zsh", "sudo"]
SUDO_OK = [
    "systemctl",
    "service",
    "netstat",
    "ss",
    "lsof",
    "ls",
]


def width():
    """width."""
    return shutil.get_terminal_size((80, 20)).columns


def height():
    """height."""
    return shutil.get_terminal_size((80, 20)).lines


MAX_ANSWER_LEN = 500


def twrap(content: str) -> str:
    """twrap.

    Args:
        content (str): content

    Returns:
        str: return wrapped string
    """
    retval = []
    for line in content.splitlines():
        line = "\n".join(
            i.ljust(width())
            for i in textwrap.wrap(
                line,
                drop_whitespace=True,
                replace_whitespace=False,
                width=width(),
            )
        )
        retval.append(line.ljust(width()))
    return "\n".join(retval)


class QuestionPrompt:
    """QuestionPrompt."""

    def __init__(self):
        """__init__."""
        HookLoader.load()
        dummy_func = getattr(events, "on_pre_spec_run_does_not_exist")
        for i in RESTRICTED:
            _name = f"on_pre_spec_run_{i}"
            setattr(events, _name, dummy_func)
        defstyle.PROMPT_TOOLKIT_STYLE.append(("bottom-toolbar", "noreverse"))
        self.xsh = globals()["__builtins__"]["__xonsh__"]
        self.nav = Navigation()
        self.xsh.env.update(
            {
                "XONSH_STORE_STDOUT": True,
                "XONSH_SHOW_TRACEBACK": True,
                "UPDATE_PROMPT_ON_KEYPRESS": True,
                "PROMPT_REFRESH_INTERVAL": 0.1,
                "BOTTOM_TOOLBAR": self._toolbar,
                "PROMPT": self.prompt,
                "SELF": self,
            }
        )
        self._all_aliases = []
        self.show_commands = False
        self.show_toolbar = True
        self.map_store = {}  # type: Dict[str,Dict]
        # pylint: disable=line-too-long
        self.map_list = lambda: [z for i in self.map_store.values() for z in i["aliases"]]  # type: ignore
        self._add_alias(["answer"], "show answer as file or text", self.answer)
        if not self.nav.no_main_intro:
            self._add_alias(
                ["b"],
                "show main introduction / help screen",
                self.nav.main_intro.run,
            )
        self._add_alias(
            ["h"],
            "hide / show available commands",
            self.toggle_command_show,
        )
        self._add_alias(
            ["i"],
            "show module intro",
            lambda: self.nav.introduction.run(),  # pylint: disable=unnecessary-lambda
        )
        self._add_alias(
            ["t"],
            "hide toolbar",
            self.toggle_toolbar,
        )
        self._add_alias(
            ["n", "j"], "next question/module", self.nav.go_next, key="next"
        )
        self._add_alias(
            ["p", "k"],
            "previous question/module",
            self.nav.go_previous,
            key="previous",
        )
        self.hostname = socket.gethostname()
        self.user = getpass.getuser()

    def toggle_toolbar(self):
        """toggle_toolbar."""
        self.show_toolbar = not self.show_toolbar

    def toggle_command_show(self):
        """toggle_command_show."""
        self.show_commands = not self.show_commands

    def auto_intro(self):
        """auto_intro."""
        if not self.nav.no_main_intro and not self.nav.seen_main_intro:
            self.nav.main_intro.run()
            self.nav.seen_main_intro = True
        if not self.nav.seen_intro:
            self.nav.introduction.run()
            self.nav.seen_intro = True

    @staticmethod
    def answer(args: List, stdin: Optional[TextIOWrapper] = None):
        """answer.

        Args:
            args (List): args
            stdin (Optional[TextIOWrapper]): stdin
        """
        if stdin is None:
            soutput = " ".join(args)
        else:
            soutput = stdin.read()  # type: ignore

        if len(soutput) > MAX_ANSWER_LEN:
            soutput = soutput[:MAX_ANSWER_LEN] + "[...]"
        s_dict = {
            "answer": soutput,
        }
        EMITTER.emit(HOOK_TYPE_ANSWER, s_dict)
        print(f"Sent:\n{color(soutput, bg='red')}")

    def command_entered(self, **kwargs):
        """command_entered.

        Args:
            kwargs:
        """
        command = kwargs["cmd"].strip()  # type: str
        if command in self.map_list():
            return
        spl = command.split()
        if spl[0] not in self._all_aliases:
            start, end = kwargs.get("ts") or (0, 0)
            time = end - start
            send_d = {
                "command": command,
                "rc": kwargs.get("rtn"),
                "output": kwargs.get("out"),
                "time": f"{time:.3f}",
            }
            send_d.update(self.nav.as_dict())
            EMITTER.emit(HOOK_TYPE_XONSH_COMMAND_ENTERED, send_d)

    @staticmethod
    def prompt() -> str:
        """prompt.

        Args:

        Returns:
            str: return prompt string
        """
        return (
            "{BOLD_GREEN}{user}@{hostname}{BOLD_BLUE} {cwd} {BOLD_BLUE}"
            " {prompt_end} {RESET}"
        )

    def _add_alias(
        self,
        alias_keys: List,
        helptxt: str,
        func: Callable,
        key: str = None,
    ):
        """_add_alias.

        Args:
            alias_keys (List): alias_keys
            helptxt (str): helptxt
            func (Callable): func
            key (str): key

        Returns:
            QuestionPrompt: returns self
        """
        join_key = "/".join(alias_keys)
        dkey = key if key else join_key
        self.map_store[dkey] = {
            "aliases": alias_keys,
            "display": join_key,
            "helptxt": helptxt,
            "func": func,
        }
        for i in alias_keys:
            self.xsh.aliases[i] = func
            self._all_aliases.append(i)
        return self

    @staticmethod
    def run_background_task(cmd: str):
        """start the process and send it into the background."""
        cmd = f'sh -c "{cmd}" &'
        subprocess.call(cmd, shell=True)

    def _toolbar(self) -> str:
        """_toolbar.

        Args:

        Returns:
            str: footer text
        """
        self.auto_intro()
        store = self.map_store.copy()
        if not any([self.nav.has_next_question, self.nav.has_next_module]):
            store.pop("next")
        if not any(
            [self.nav.has_previous_module, self.nav.has_previous_question]
        ):
            store.pop("previous")

        passed_map = {dct["display"]: dct["helptxt"] for dct in store.values()}
        return NavFooter.get(
            self.nav, passed_map, self.show_toolbar, self.show_commands
        )


# notice the decorators, these are restricted command
# dummy decorator for dynamically filtering commands see RESTRICTED variable
# I know these are feeble attempts, it's not going to stop a hacker
@events.on_pre_spec_run_does_not_exist
def bash_filter(**kwargs) -> None:
    """bash_filter.

    Restricted stuff is here

    Args:
        kwargs:
    """
    spec = kwargs["spec"]  # type: SubprocSpec
    xsh = globals()["__builtins__"]["__xonsh__"]
    iface = xsh.env["SELF"]  # type: QuestionPrompt
    run_cmd = " ".join(spec.cmd)
    send_d = {
        "command": run_cmd,
    }
    send_d.update(iface.nav.as_dict())
    EMITTER.emit(HOOK_TYPE_QUESTIONABLE, send_d)
    cstr = " ".join(
        [
            chr(127367),
            "restricted",
        ]
    )
    repl_seq = ["echo", color(cstr, bg="red")]
    _bin = spec.cmd[0]
    rest_conds = any(
        [
            (_bin == "sudo" and spec.cmd[1] not in SUDO_OK),
            (_bin in RESTRICTED and _bin != "sudo"),
        ]
    )
    if rest_conds:
        spec.cmd = repl_seq


@events.on_postcommand
def cmd_event(**kwargs) -> None:
    """cmd_event.

    Args:
        kwargs:
    """
    xsh = globals()["__builtins__"]["__xonsh__"]
    iface = xsh.env["SELF"]  # type: QuestionPrompt
    iface.command_entered(**kwargs)
