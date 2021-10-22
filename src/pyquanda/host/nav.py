#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Navigation related utils."""

import json
from json.decoder import JSONDecodeError
from typing import Any, Dict, List

import colors
from rich import box
from rich.align import Align
from rich.columns import Columns
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table  # type: ignore
from rich.text import Text
from pyquanda.exceptions import PreCheckFail
from pyquanda.hooks.config import (
    ASYNC_EMITTER,
    HOOK_TYPE_NAV_NEXT,
    HOOK_TYPE_NAV_PREVIOUS,
)
from pyquanda.host.intro import Intro, intro_load_pickle_b64
from pyquanda.host.main_intro_data import MainIntroCollection
from pyquanda.host.question_data import QuestionCollection
from pyquanda.host.question_state import StateData


def color(color_name: str, txt: str) -> str:
    """color.

    Args:
        color_name (str): color
        txt (str): txt

    Returns:
        str: color ansi
    """
    return colors.color(txt, fg=color_name)


class Navigation:
    """Navigation."""

    def __init__(self):
        """__init__."""
        self.questions = QuestionCollection()
        self._main_intro = MainIntroCollection()

        self.questions.load()
        self._main_intro.load()
        _mintro_len = len(self._main_intro.REGISTRY)
        if _mintro_len >= 2:
            raise PreCheckFail(
                f"Main intro should only have 0-1 entries, {_mintro_len} was"
                " given"
            )
        self.modules = list(
            sorted(
                (i for i in self.questions.REGISTRY.values()),
                key=lambda i: i.order,
            )
        )
        self.state = StateData()
        self._all_questions = []
        self.intros = {}
        # no main intro was given, so we're skipping it
        self.no_main_intro = _mintro_len == 0

    def _place_wrap(self, key: str, default_value: Any) -> Any:
        """_place_wrap.

        Args:
            key (str): key
            default_value (Any): default_value

        Returns:
            Any: Returns default value or defined value
        """
        place = self.state.get(key, required=False)  # type: Any
        if place:
            return place
        self.state.set(key, default_value)
        return default_value

    @property
    def current_module_index(self):
        """current_module_index."""
        return int(self._place_wrap("module_place", 0))

    @current_module_index.setter
    def current_module_index(self, value):
        """current_module_index.

        Args:
            value:
        """
        self.state.set("module_place", value)

    @property
    def current_question_index(self):
        """current_question_index."""
        return self._place_wrap("question_place", 0)

    @current_question_index.setter
    def current_question_index(self, value):
        """current_question_index.

        Args:
            value:
        """
        self.state.set("question_place", value)

    @property
    def seen_intro(self):
        """seen_intro."""
        key = f"intro_{self.current_module_index}_seen"
        return self._place_wrap(key, False)

    @seen_intro.setter
    def seen_intro(self, value):
        """seen_intro.

        Args:
            value:
        """
        key = f"intro_{self.current_module_index}_seen"
        self.state.set(key, value)

    @property
    def seen_main_intro(self):
        """seen_main_intro."""
        key = "intro_main_seen"
        return self._place_wrap(key, False)

    @seen_main_intro.setter
    def seen_main_intro(self, value):
        """seen_main_intro.

        Args:
            value:
        """
        key = "intro_main_seen"
        self.state.set(key, value)

    @property
    def percentage(self) -> int:
        """percentage.

        Args:

        Returns:
            int:
        """
        curloc = self.all_questions.index(self.key) + 1
        return int((curloc / len(self.all_questions)) * 100)

    @staticmethod
    def _fmt_of(curval: int, all_vals: List) -> str:
        """_fmt_of.

        Args:
            curval (int): curval
            all_vals (List): all_vals

        Returns:
            str: return x of y for index
        """
        x, y = str(curval + 1), str(len(all_vals))
        return f"[{x.ljust(2)} of {y.rjust(2)}]"

    @property
    def mod_x_of_y(self):
        """mod_x_of_y."""
        return self._fmt_of(self.current_module_index, self.modules)

    @property
    def question_x_of_y(self):
        """question_x_of_y."""
        return self._fmt_of(
            self.current_question_index, self.current_question_set
        )

    @property
    def key(self):
        """key."""
        return f"{self.current_module_name}/{self.current_question}"

    @property
    def all_questions(self):
        """all_questions."""
        if self._all_questions:
            return self._all_questions
        self._all_questions = [
            f"{i.module_name}/{q}" for i in self.modules for q in i.questions  # type: ignore
        ]
        return self._all_questions

    @property
    def current_module_name(self) -> str:
        """current_module_name.

        Args:

        Returns:
            str:
        """
        return self.modules[self.current_module_index].module_name

    @property
    def background_commands(self) -> List:
        """background_commands.

        Args:

        Returns:
            List:
        """
        return self.modules[self.current_module_index].question_background_cmds

    @property
    def current_question_set(self) -> List:
        """current_question_set.

        Args:

        Returns:
            List:
        """
        return self.modules[self.current_module_index].questions  # type: ignore

    @property
    def main_intro(self) -> Intro:
        """main_intro.

        Args:

        Returns:
            Intro:
        """
        mods = list(self._main_intro.REGISTRY.values())
        return mods[0].introduction

    @staticmethod
    def _introduction(introduction_b64: str) -> Intro:
        """_introduction.

        Args:
            introduction_b64 (str): introduction_b64

        Returns:
            Intro: Introduction object
        """
        return intro_load_pickle_b64(introduction_b64)

    @property
    def introduction(self) -> Intro:
        """introduction.

        Args:

        Returns:
            Intro:
        """
        return self.modules[self.current_module_index].introduction

    @property
    def description(self) -> str:
        """description.

        Args:

        Returns:
            str:
        """
        return self.introduction.title

    @property
    def current_question(self) -> str:
        """current_question.

        Args:

        Returns:
            str:
        """
        return self.current_question_set[self.current_question_index]

    @property
    def has_previous_question(self):
        """has_previous_question."""
        if self.current_question_index - 1 < 0:
            return False
        return True

    @property
    def has_next_question(self):
        """has_next_question."""
        if (
            self.current_question_index + 1
            > len(self.current_question_set) - 1
        ):
            return False
        return True

    @property
    def has_next_module(self):
        """has_next_module."""
        if self.current_module_index + 1 > len(self.modules) - 1:
            return False
        return True

    @property
    def has_previous_module(self):
        """has_previous_module."""
        if self.current_module_index - 1 < 0:
            return False
        return True

    def go_next(self):
        """next."""
        do_hook = True
        if self.has_next_question:
            self.current_question_index += 1
        elif self.has_next_module:
            self.current_module_index += 1
            self.current_question_index = 0
        else:
            do_hook = False
            print(color("red", "No more modules or questions"))
        if do_hook:
            ASYNC_EMITTER.emit(HOOK_TYPE_NAV_NEXT, self.as_dict())

    def go_previous(self):
        """previous."""
        do_hook = True
        if self.has_previous_question:
            self.current_question_index -= 1
        elif self.has_previous_module:
            self.current_module_index -= 1
            self.current_question_index = len(self.current_question_set) - 1
        else:
            do_hook = False
            print(color("red", "You are on the first module / question"))
        if do_hook:
            ASYNC_EMITTER.emit(HOOK_TYPE_NAV_PREVIOUS, self.as_dict())

    def as_dict(self) -> Dict[str, str]:
        """as_dict.

        Args:

        Returns:
            Dict[str, str]: object dict representation
        """
        retvals = {}
        for i in dir(self):
            attr = getattr(self, i)
            if any(
                [
                    i.startswith("_"),
                    callable(getattr(self, i)),
                ]
            ):
                continue
            try:
                json.dumps(attr)
            except (
                JSONDecodeError,
                TypeError,
            ):
                continue
            retvals[i] = attr
        return retvals


class NavFooter:
    """NavFooter."""

    @staticmethod
    def get(
        nav: Navigation,
        command_map: Dict[str, str],
        show: bool,
        show_cmds: bool,
    ) -> str:
        """get.

        Args:
            nav (Navigation): nav
            command_map (Dict[str, str]): command_map
            show (bool): show
            show_cmds (bool): show_cmds

        Returns:
            str: navigation footer
        """
        STYLE1 = "on blue"
        STYLE2 = "on grey37"
        STYLE3 = "i white"
        console = Console()
        toggle_hide_txt = '[bold green]"h"[/] to close'
        toggle_display_txt = 'enter "h" to show help, "t" to hide this toolbar'
        table = Table(
            title=f"Available Commands ({toggle_hide_txt})",
            box=box.MINIMAL,
            style="white",
        )
        table.show_lines = False
        table.add_column("command")
        table.add_column("description")
        table.show_header = False
        for k, v in command_map.items():
            table.add_row(Text(k, style="red bold"), Text(v, style="italic"))

        title_txt = f"[{STYLE3}]Module: {nav.mod_x_of_y}[/]"

        if show:
            contents = [
                Panel(
                    f"[b]{nav.description}[/]",
                    style=STYLE1,
                    title=title_txt,
                    subtitle=f"[{STYLE3}]Question: {nav.question_x_of_y}[/]",
                    title_align="right",
                    subtitle_align="right",
                ),
                Panel(
                    nav.current_question,
                    style=STYLE2,
                    box=box.MINIMAL,
                ),
            ]
            if show_cmds:
                contents.append(Align(table, "center"))  # type: ignore
            else:
                contents.append(Align(toggle_display_txt, "center"))  # type: ignore
        else:
            cur_cmd = " ".join(
                [
                    i.strip()
                    for i in nav.current_question.splitlines()
                    if i.strip()
                ]
            ).strip()
            contents = [
                Panel(
                    Columns(
                        [
                            Align('Press "t" to show toolbar', "left"),
                            Align(
                                Text(
                                    cur_cmd, overflow="ellipsis", no_wrap=True
                                ),
                                "right",
                            ),
                        ],
                        expand=True,
                    ),
                    style=STYLE1,
                )
            ]
        with console.capture() as capture:
            console.print(Group(*contents))
        return capture.get()
