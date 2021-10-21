#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate documentation for project."""

import sys
from argparse import ArgumentParser
from importlib import import_module
from pathlib import Path
from typing import Any, Dict

from freeplane_tools.github import MindMap2GithubMarkdown

ME = Path(__file__)
BASE = Path(__file__).resolve().parent.parent
BINDIR = BASE.joinpath("bin")
README = BASE.joinpath("README.mm")
DEST_README = BASE.joinpath("README.md")
sys.path.append(str(BINDIR.absolute()))


GITHUB_BASE = "https://github.com/shollingsworth/pyquanda/blob/main"
GITHUB_RAW = "https://github.com/shollingsworth/pyquanda/raw/main"


def code_section(txt):
    """Code section."""
    val = []
    val.append(
        "\n".join(
            [
                "```",
                txt,
                "```",
            ]
        )
    )
    return "\n".join(val)


def getdesc(file: Path):
    """Get description."""

    content = file.read_text()
    arr = content.splitlines()
    for i in arr:
        _a2 = i.split("=")
        if len(_a2) != 2:
            continue
        name, desc = _a2
        if name != "DESC":
            continue
        return desc.strip('"')
    return None


def main():
    """Run main function."""
    pycmd = import_module("pyquanda-cmd")  # type: Any
    parent = pycmd.parent  # type: Any
    subcmds = parent.subparser.choices  # type: Dict[str, ArgumentParser]
    repl_map = {
        "__HELP__": [],
    }
    repl_map["__HELP__"].append("# Main")

    for subcmd, subp in subcmds.items():
        repl_map["__HELP__"].append(f"## {subcmd}")
        repl_map["__HELP__"].append(code_section(subp.format_help()))

    obj = MindMap2GithubMarkdown(str(README))
    data = obj.get_document()
    for k, arr in repl_map.items():
        data = data.replace(k, "\n".join(arr))

    with DEST_README.open("wb") as fileh:
        fileh.write(data.encode())
        fileh.flush()

    print(DEST_README.read_text())


if __name__ == "__main__":
    main()
