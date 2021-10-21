#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main Ansible Module Builder."""
# pylint: disable=unused-argument

import json
import os
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List

import ansible_runner
from ruamel.yaml import YAML

from pyquanda.exceptions import PreCheckFail
from pyquanda.hooks.registry import HookLoader
from pyquanda.hooks.config import EMITTER
from pyquanda.hooks.config import (
    HOOK_TYPE_ANSIBLE_EVENT,
    HOOK_TYPE_ANSIBLE_RUNBOOK_COMPLETE,
)

_POP_KEYS = ["env", "ansible_facts"]

_yaml = YAML()

_BASE = Path(__file__).parent
_SITE_YAML_FILE = _BASE.joinpath("playbook/site.yaml")


_HOSTS = """
[all]
localhost
""".lstrip()

EVENT_FAILURE = "runner_on_failed"
EVENT_OK = "runner_on_ok"
EVENT_RUNBOOK_DONE = "successful"


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
        HookLoader.load()
        self._verify(path)
        self.path = path
        self.name = self.path.name.title()
        self.playbook = list(_yaml.load(_SITE_YAML_FILE.read_bytes()))
        self.playbook[0]["name"] = self.name
        self.python_interp = shutil.which("python3")

    def status_handler(self, args: Dict, **kwargs):  # type: ignore
        """status_handler.

        Args:
            args: ansible event args
            kwargs: Not used
        """
        # gd linter
        _ = kwargs
        status = args["status"]
        if status == EVENT_RUNBOOK_DONE:
            send_d = {
                "runbook": self.name,
                "status": "complete",
            }
            EMITTER.emit(HOOK_TYPE_ANSIBLE_RUNBOOK_COMPLETE, send_d)
        print(f"runbook {status=}, {self.name=}")

    def event_handler(self, evt_dct: Dict):
        """event_handler.

        Args:
            evt_dct (Dict): evt_dct
        """
        respond = ["runner_on_ok", "runner_on_failed"]
        evt = evt_dct["event"]
        if evt not in respond:
            return
        data = evt_dct.get("event_data", {})
        res = data.get("res", {})
        for key in _POP_KEYS:
            if key in data:
                data.pop(key)
            if key in res:
                res.pop(key)
        send_d = {
            "runbook": self.name,
            "event": evt,
            "res": res,
        }
        EMITTER.emit(HOOK_TYPE_ANSIBLE_EVENT, send_d)
        print("event", json.dumps(evt_dct, indent=4, separators=(",", " : ")))

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
            hosts_file.write_text(_HOSTS)
            self._copy_src_role_to_dest_dir(self.path, role_dir)
            pb_file = tdir.joinpath("site.yaml")
            cfg = tdir.joinpath("ansible.cfg")
            cfg.write_text(
                "\n".join(
                    [
                        "[defaults]",
                        f"interpreter_python={self.python_interp}",
                    ]
                )
            )
            os.environ["ANSIBLE_CONFIG"] = str(cfg)
            with pb_file.open("wb") as fileh:
                _yaml.dump(self.playbook, fileh)
            # run status for the kickoff TODO
            syspath = os.environ["PATH"]
            syspath += ":/usr/local/bin"
            inv = {"all": {"hosts": {"localhost": None}}}
            ansible_runner.run(
                event_handler=self.event_handler,
                status_handler=self.status_handler,
                settings={
                    "suppress_ansible_output": True,
                },
                inventory=inv,
                playbook=str(pb_file),
                envvars={
                    "PATH": syspath,
                },
            )
            #  events = []
            #  for each_host_event in run.events:  # type: ignore
            #      events.append(each_host_event)
            #  print(f"{run.status=} / {run.rc=}")
            #  print(f"Final status: {run.stats}")  # type: ignore

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
