#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Introduction builder."""
from pathlib import Path
import pickle
from abc import ABC
from base64 import b64decode, b64encode
from typing import Any, Callable, Dict, List
from jinja2 import Template

from rich import box
from rich import print as bprint
from rich.align import Align
from rich.color import ANSI_COLOR_NAMES
from rich.console import Console
from rich.padding import Padding
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table  # type: ignore
from rich.text import Text
from rich.theme import Theme

from pyquanda.exceptions import PreCheckFail


def show_all_colors() -> None:
    """show_all_colors.

    Args:

    Returns:
        None:
    """
    table = Table()
    table.title = "color map"
    table.add_column("on")
    table.add_column("solo")

    def pstyle(col: str) -> List[Text]:
        """pstyle.

        Args:
            col (str): col

        Returns:
            List[Text]: list of Text objects
        """
        return [
            Text(st, style=st)
            for st in [
                f"on {col}",
                f"{col}",
            ]
        ]

    for col in sorted(ANSI_COLOR_NAMES.keys()):
        table.add_row(*pstyle(col))
    bprint(table)


class _Base(ABC):
    """_Base."""

    ST_MAIN_TITLE = "bold on blue"
    ST_TITLE = "on grey35 bold"
    ST_FOOTER = "on blue"
    THEME = Theme(
        {
            "code": "dim cyan",
            "warning": "magenta",
            "url": "bold red",
        }
    )

    def __init__(self):
        """__init__."""
        self._console = None
        self._header_elements = []
        self._main_elements = []
        self._template_path = Path("/tmp")
        self._config = {}

    @staticmethod
    def PADDING(el: Any) -> Padding:
        """PADDING.

        Args:
            el (Any): el

        Returns:
            Padding: pad object
        """
        return Padding(el, pad=(1, 1))

    @staticmethod
    def _get_panel(txt: str, style: str, **kwargs) -> Panel:
        """_get_panel.

        Args:
            txt (str): txt
            style (str): style
            kwargs:

        Returns:
            Panel: pane object
        """
        h = len(txt.splitlines()) + 2
        return Panel(
            Text(txt, justify="center"),
            height=h,
            style=style,
            **kwargs,
        )

    @property
    def console(self) -> Console:
        """console.

        Args:

        Returns:
            Console:
        """
        if not self._console:
            self._console = Console(theme=self.THEME)
        return self._console

    def header(self, header_txt: str) -> None:
        """header.

        Args:
            header_txt (str): header_txt
        """
        self._main_elements.append(self._get_panel(header_txt, self.ST_TITLE))

    def get_code(self, code_dct: Dict) -> Syntax:
        """get_code.

        Args:
            code_dct (Dict): code_dct

        Returns:
            Syntax: code syntax object syntax
        """
        code_type = code_dct["type"]
        code_txt = code_dct["value"]
        possible_code_file = self._template_path.joinpath(code_txt)
        if possible_code_file.exists():
            code_txt = possible_code_file.read_text()
        return Syntax(code_txt, code_type)

    def code(self, code_dct: Dict) -> None:
        """code.

        Args:
            code_dct (Dict): code_dct
        """
        self._main_elements.append(self.get_code(code_dct))

    def txt(self, text: str) -> None:
        """txt.

        Args:
            text (str): text
        """
        self._main_elements.append(text)

    def j2(self, filename: str) -> None:
        """j2.

        Args:
            filename (str): filename
        """
        fpath = self._template_path.joinpath(filename)
        cont = Template(fpath.read_text())  # type: Template
        self._main_elements.append(cont.render(**self._config))

    def _get_func(self, attr_name: str) -> Callable:
        """_get_func.

        Args:
            attr_name (str): attr_name

        Returns:
            Callable: callable wrapper function
        """
        return getattr(self, attr_name)

    def table(self, dct: Dict) -> None:
        """table.

        Args:
            dct (Dict): dct

        Returns:
            None:
        """
        table = Table(box=box.DOUBLE_EDGE)
        func_map = {}

        def repl_args(args: Dict[str, str], value: str) -> Dict:
            """repl_args.

            Args:
                args (Dict): args
                value (str): value
            Returns:
                Dict: key value dict for substituted arguments
            """
            retval = {
                k: v if v != "__value__" else value for k, v in args.items()
            }
            return retval

        def run_val(func: Callable, value: str, kwargs: Dict[str, str]) -> Any:
            return func(repl_args(kwargs, value))

        for k, v in dct["row_map"].items():
            func_key = v["func"]
            margs = v["args"]
            func = self._get_func(func_key)
            func_map[k] = {
                "func": func,
                "args": margs,
            }

        table.title = dct["title"]
        for i in dct["headers"]:
            table.add_column(i)

        for rdct in dct["rows"]:
            row = []
            for k, v in rdct.items():
                func = func_map[k]["func"]
                args = func_map[k]["args"]
                row.append(run_val(func, v, args))
            table.add_row(*row)
        self._main_elements.append(Align(table, align="center"))


class Intro(_Base):
    """Intro."""

    def __init__(self, title: str, template_path: Path, config: Dict):
        """__init__.

        Args:
            title (str): title
            template_path (Path): template_path
            config (Dict): config
        """
        super().__init__()
        self._template_path = template_path
        self._main_title = title
        self._config = config
        self._header_elements.append(
            self._get_panel(
                self.title.upper(),
                self.ST_MAIN_TITLE,
                subtitle="press q to exit",
                subtitle_align="left",
            )
        )

    def load(self, datafile: Path, values: List[Dict[str, str]]) -> None:
        """load.

        Args:
            datafile (Path): datafile
            values (List[Dict[str, str]]): values

        Raises:
            PreCheckFail: if validation fails
        """
        for dct in values:
            _type = dct["type"]
            content = dct["content"]
            func = self._get_func(_type)
            try:
                func(content)
            except Exception as _e:
                raise PreCheckFail(
                    f"Found issue with datafile {datafile}"
                ) from _e

    @property
    def title(self) -> str:
        """title.

        Args:

        Returns:
            str:
        """
        return self._main_title

    def run(self) -> None:
        """run."""
        with self.console.pager(styles=True):
            self.console.print(*map(Intro.PADDING, self._header_elements))
            self.console.print(*map(Intro.PADDING, self._main_elements))


def intro_load_pickle_b64(b64: str) -> Intro:
    """intro_load_pickle_b64.

    Args:
        b64 (str): b64

    Returns:
        Intro: intro object
    """
    return pickle.loads(b64decode(b64))


def intro_export_b64(intro: Intro) -> str:
    """intro_export_b64.

    Args:
        intro (Intro): intro

    Returns:
        str: exported b64 encoded intro object
    """
    return b64encode(pickle.dumps(intro)).decode()
