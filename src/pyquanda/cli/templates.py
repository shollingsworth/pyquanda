#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Templates for creating new modules."""
import shutil
import tempfile
from distutils.dir_util import copy_tree
from pathlib import Path
from typing import Iterator, Tuple

from pyquanda.exceptions import PreCheckFail

_BASE = Path(__file__).parent.joinpath("data")
TYPES = [i.name for i in _BASE.iterdir() if i.is_dir() and i.name != "common"]
COMMON_DIR = _BASE.joinpath("common")


def _mod_files(
    path: Path, name: str, description: str
) -> Iterator[Tuple[Path, bytes]]:
    """_mod_files.

    Args:
        path (Path): path
        name (str): name
        description (str): description

    Returns:
        Iterator[Tuple[Path, bytes]]: file / replaced content
    """
    stubs = {
        b"__NAME__": name.encode(),
        b"__DESCRIPTION__": description.encode(),
    }
    for i in path.iterdir():
        if i.is_dir():
            yield from _mod_files(i, name, description)
        else:
            cont = i.read_bytes()
            for repl, value in stubs.items():
                cont = cont.replace(repl, value)
            yield i, cont


def _copy_dir(src: Path, stage: Path):
    """_copy_dir.

    Args:
        src (Path): src
        stage (Path): stage
    """
    for path in src.iterdir():
        dest = stage.joinpath(path.name)
        if path.is_dir():
            print(f"copying {dest} dir")
            copy_tree(str(path), str(dest))
        else:
            print(f"copying {dest} file")
            shutil.copy(path, dest)


def copy_type(_type, dest: Path, name: str, description: str):
    """copy_type.

    Args:
        _type:
        dest (Path): dest
        name (str): name
        description (str): description

    Raises:
        PreCheckFail: on error
    """
    par = dest.parent
    if not (par.exists() and par.is_dir()):
        raise PreCheckFail(f"{dest} is an invalid destination")
    with tempfile.TemporaryDirectory() as tdir:
        type_src = _BASE.joinpath(_type)
        if not (type_src.exists() and type_src.is_dir()):
            raise PreCheckFail(f"{_type} is an invalid source")
        tempdir = Path(tdir)
        stage = tempdir.joinpath("stage")
        stage.mkdir()
        _copy_dir(COMMON_DIR, stage)
        _copy_dir(type_src, stage)
        for fpath, content in _mod_files(stage, name, description):
            fpath.write_bytes(content)
        copy_tree(str(stage), str(dest))
