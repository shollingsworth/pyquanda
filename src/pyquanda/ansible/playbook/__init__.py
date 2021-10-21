#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main Ansible Module Builder."""

import os
import shutil
import tempfile
from pathlib import Path
from typing import List

import ansible_runner
from ruamel.yaml import YAML

from pyquanda.exceptions import PreCheckFail

yaml = YAML()

_BASE = Path(__file__).parent
SITE_YAML_FILE = _BASE.joinpath("site.yaml")


HOSTS = """
[all]
localhost
""".lstrip()


class Ansible:
    """Ansible."""

    DIR_HANDLER = "handler"
    DIR_TASKS = "tasks"
    DIR_TEMPLATE = "templates"

    MK_MAINS = [
        DIR_HANDLER,
        DIR_TASKS,
    ]

    def __init__(self, path: Path) -> None:
        """__init__.

        Args:
            path (Path): path

        Returns:
            None:
        """
        self._verify(path)
        self.path = path
        self.playbook = yaml.load(SITE_YAML_FILE.read_bytes())

    @classmethod
    def copy_dirs(cls) -> List[str]:
        """copy_dirs.

        Args:

        Returns:
            List[str]: list of directory strings
        """
        return [getattr(cls, i) for i in dir(cls) if i.startswith("DIR_")]

    def _copy_src_role_to_dest_dir(
        self, src_mod_path: Path, dst_roles_dir: Path
    ):
        """_copy_src_role_to_dest_dir.

        Args:
            src_mod_path (Path): src_mod_path
            dst_roles_dir (Path): dst_roles_dir

        Raises:
            PreCheckFail: on validation error
        """
        bname = src_mod_path.absolute().name
        src_config_file = src_mod_path.joinpath("vars.yaml")
        dst_config_file = dst_roles_dir.joinpath("vars.yaml")
        try:
            shutil.copy(src_config_file, dst_config_file)
        except FileNotFoundError:
            pass
        self.playbook[0]["roles"].append(str(bname))
        dst_dir = dst_roles_dir.absolute().joinpath(bname)
        for req_dir in self.copy_dirs():
            to_dir = dst_dir.joinpath(req_dir)
            src_dir = src_mod_path.joinpath(req_dir)
            try:
                shutil.copytree(src_dir, to_dir)
            except (
                FileExistsError,
                FileNotFoundError,
            ) as _e:
                msg = "\n".join(
                    [
                        f"src: {req_dir}",
                        f"dst: {dst_dir}",
                    ]
                )
                raise PreCheckFail(msg) from _e

    def run(self):
        """run."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tdir = Path(tmpdir)
            role_dir = tdir.joinpath("roles")
            role_dir.mkdir()
            hosts_file = tdir.joinpath("hosts")
            hosts_file.write_text(HOSTS)
            self._copy_src_role_to_dest_dir(self.path, role_dir)
            pb_file = tdir.joinpath("site.yaml")
            with pb_file.open("wb") as fileh:
                yaml.dump(self.playbook, fileh)
            # run status for the kickoff TODO
            syspath = os.environ["PATH"]
            syspath += ":/usr/local/bin"
            inv = {"all": {"hosts": {"localhost": None}}}
            pyint = shutil.which("python3")
            print(pyint)
            run = ansible_runner.run(
                ansible_python_interpreter=pyint,
                inventory=inv,
                playbook=str(pb_file),
                envvars={
                    "PATH": syspath,
                },
            )
            print("{}: {}".format(run.status, run.rc))
            print("Final status:")
            print(run.stats)  # type: ignore

    def _verify(self, path: Path):
        """_verify.

        Args:
            path (Path): path

        Raises:
            PreCheckFail: on validation error
        """
        for i in self.copy_dirs():
            dpath = path.joinpath(i)
            if not dpath.exists():
                raise PreCheckFail(f"Path {dpath} does not exist")
            if not dpath.is_dir():
                raise PreCheckFail(f"Path {dpath} is not a directory")
        for i in self.MK_MAINS:
            mfile = path.joinpath(i, "main.yaml")
            if not mfile.exists():
                raise PreCheckFail(f"file {i} does not exist")
