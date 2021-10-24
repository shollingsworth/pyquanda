#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Helper lib for yaml."""
# from io import StringIO
from pathlib import Path
from typing import Any, IO
from yaml import load, dump
from yaml.loader import SafeLoader


def load_from_path(file: Path) -> Any:
    """load_from_path.

    Args:
        file (Path): file

    Returns:
        Union[List, Dict]: yaml doc
    """
    return load(file.read_bytes(), Loader=SafeLoader)


def load_from_bytes(sio: bytes) -> Any:
    """load_from_bytes.

    Args:
        sio (bytes): sio

    Returns:
        Union[List, Dict]: value
    """
    return load(sio, Loader=SafeLoader)


def dump_to_file_open(obj: Any, file: IO):
    """dump_to_file_open.

    Args:
        obj (Any): obj
        file (BinaryIO): file
    """
    dump(obj, file)


def dump_to_text(obj: Any) -> str:
    """dump_to_text.

    Args:
        obj (Any): obj

    Returns:
        str: yaml text output
    """
    return dump(obj)


#  def load_from_path(file: Union[Path, bytes]) -> Any:
#      """load_from_path.
#
#      Args:
#          file (Path): file
#
#      Returns:
#          Union[List, Dict]: yaml doc
#      """
#      return YAML().load(file)
#
#
#  def dump_to_file_open(obj: Any, file: BinaryIO):
#      """dump_to_file_open.
#
#      Args:
#          obj (Any): obj
#          file (BinaryIO): file
#      """
#      YAML.dump(obj, file)
#
#
#  def dump_to_text(obj: Any) -> str:
#      """dump_to_text.
#
#      Args:
#          obj (Any): obj
#
#      Returns:
#          str: yaml text output
#      """
#      with StringIO() as sio:
#          YAML.dump(obj, sio)
#          return sio.getvalue()
