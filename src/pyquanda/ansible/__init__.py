#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main Ansible Module Builder."""
# pylint: disable=unused-argument,missing-function-docstring

import json
import os
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List

import ansible_runner

from pyquanda.exceptions import PreCheckFail
from pyquanda.hooks.registry import HookLoader
from pyquanda.hooks.config import SYNC_EMITTER
from pyquanda.hooks.config import (
    HOOK_TYPE_ANSIBLE_EVENT,
    HOOK_TYPE_ANSIBLE_RUNBOOK_COMPLETE,
)
from pyquanda.lib.yaml_util import dump_to_file_open, load_from_path

_POP_KEYS = ["env", "ansible_facts"]

_BASE = Path(__file__).parent
_SITE_PLAY_FILE = _BASE.joinpath("play.yaml")

SUPRESS_OUTPUT = False


_HOSTS = """
[all]
localhost
""".lstrip()

EVENT_FAILURE = "runner_on_failed"
EVENT_OK = "runner_on_ok"


class Ansible:
    """Ansible."""

    DIR_HANDLER = "handlers"
    DIR_TASKS = "tasks"
    DIR_TEMPLATE = "templates"

    MK_MAINS = [
        DIR_HANDLER,
        DIR_TASKS,
    ]
    PYTHON_INTERP = shutil.which("python3")

    @classmethod
    def event_handler(cls, evt_dct: Dict) -> bool:
        respond = [
            EVENT_FAILURE,
            # EVENT_OK,
        ]
        evt = evt_dct["event"]
        if evt not in respond:
            return True

        data = evt_dct.get("event_data", {})
        ignore_errors = data.get("ignore_errors", False)
        if ignore_errors:
            return True

        if "res" in data:
            res = data.pop("res")
        else:
            res = {}
        for key in _POP_KEYS:
            if key in data:
                data.pop(key)
            if key in res:
                res.pop(key)
        send_d = {
            "event": evt,
            "data": data,
            "res": res,
        }
        # for debugging later
        #  import json
        #
        #  print("*" * 100)
        #  print(ignore_errors)
        #  print(json.dumps(send_d, indent=4, separators=(",", " : ")))
        #  print("*" * 100)
        SYNC_EMITTER.emit(HOOK_TYPE_ANSIBLE_EVENT, send_d)
        return True

    @classmethod
    def copy_dirs(cls) -> List[str]:
        """copy_dirs.

        Args:

        Returns:
            List[str]: list of directory strings
        """
        return [getattr(cls, i) for i in dir(cls) if i.startswith("DIR_")]

    @classmethod
    def _copy_src_role_to_dest_dir(
        cls, src_mod_path: Path, dst_roles_dir: Path
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
        dst_dir = dst_roles_dir.absolute().joinpath(bname)
        for req_dir in cls.copy_dirs():
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

    @classmethod
    def run_single(cls, module_path: Path, debug_only: bool):
        """run."""
        cls._run(module_path, is_all=False, debug_only=debug_only)

    @classmethod
    def _get_sorted_module_paths(cls, paths: List[Path]) -> List[Path]:
        def _sort(path):
            cfg = path.joinpath("config.yaml")
            obj = load_from_path(cfg)
            return obj["order"]

        errors = []
        mod_paths = []  # type: List[Path]
        for i in sorted(paths, key=_sort):
            try:
                cls._verify(i)
                mod_paths.append(i)
            except PreCheckFail as _e:
                errors.append(_e)
        if errors:
            msg = ",".join(str(i) for i in errors)
            raise PreCheckFail(msg)
        return mod_paths

    @classmethod
    def _get_playbook(cls, path: Path):
        var_file = path.joinpath("vars.yaml")
        config_file = path.joinpath("config.yaml")

        cfg_obj = load_from_path(config_file)  # type: Dict
        if var_file.exists():
            vobj = load_from_path(var_file)
            cfg_obj.update(vobj)

        pb = load_from_path(_SITE_PLAY_FILE.read_bytes())  # type: Dict
        pb["name"] = path.name.title()
        task = {
            "block": [
                {
                    "include_role": {
                        "name": path.name,
                    },
                    "vars": cfg_obj,
                },
            ],
            "rescue": [
                {
                    "debug": {
                        "msg": "Play failed",
                    },
                },
                {
                    "meta": "clear_host_errors",
                },
                {
                    "meta": "end_play",
                },
            ],
        }
        pb["tasks"].append(task)
        # print(json.dumps(pb, indent=4, separators=(",", " : ")))
        return pb

    @classmethod
    def _run(cls, path: Path, is_all: bool, debug_only: bool):
        """run."""
        HookLoader.load()
        mod_paths = []
        errors = []
        playbooks = []

        if is_all:
            mvals = [
                i
                for i in path.iterdir()
                if (i.is_dir() and not i.name.startswith("_"))
            ]
            mod_paths = cls._get_sorted_module_paths(mvals)
        else:
            mod_paths = cls._get_sorted_module_paths([path])

        if errors:
            msg = ",".join(str(i) for i in errors)
            raise PreCheckFail(msg)

        for i in mod_paths:
            playbooks.append(cls._get_playbook(i))

        if debug_only:
            print(json.dumps(playbooks, indent=4, separators=(",", " : ")))
        else:
            with tempfile.TemporaryDirectory() as tmpdir:
                tdir = Path(tmpdir)
                role_dir = tdir.joinpath("roles")
                role_dir.mkdir()
                hosts_file = tdir.joinpath("hosts")
                hosts_file.write_text(_HOSTS)
                for i in mod_paths:
                    cls._copy_src_role_to_dest_dir(i, role_dir)

                cfg = tdir.joinpath("ansible.cfg")
                cfg.write_text(
                    "\n".join(
                        [
                            "[defaults]",
                            f"interpreter_python={cls.PYTHON_INTERP}",
                        ]
                    )
                )
                os.environ["ANSIBLE_CONFIG"] = str(cfg)
                pb_file = tdir.joinpath("site.yaml")
                with pb_file.open("wb") as fileh:
                    dump_to_file_open(playbooks, fileh)
                # run status for the kickoff TODO
                syspath = os.environ["PATH"]
                syspath += ":/usr/local/bin"
                inv = {"all": {"hosts": {"localhost": None}}}
                run = ansible_runner.run(
                    event_handler=cls.event_handler,
                    # status_handler=cls.status_handler,
                    settings={
                        "suppress_ansible_output": SUPRESS_OUTPUT,
                    },
                    inventory=inv,
                    playbook=str(pb_file),
                    envvars={
                        "PATH": syspath,
                    },
                )
                stats = {
                    k: 0 if not v.values() else list(v.values())[0]
                    for k, v in run.stats.items()  # type: ignore
                }
                send_d = {
                    "status": run.status,  # type: ignore
                    "rc": run.rc,  # type: ignore
                    "stats": stats,
                }
                SYNC_EMITTER.emit(HOOK_TYPE_ANSIBLE_RUNBOOK_COMPLETE, send_d)

    @classmethod
    def run_all(cls, modules_directory: Path, debug_only: bool):
        """run."""
        cls._run(modules_directory, is_all=True, debug_only=debug_only)

    @classmethod
    def _verify(cls, path: Path):
        """_verify.

        Args:
            path (Path): path

        Raises:
            PreCheckFail: on validation error
        """
        for i in cls.copy_dirs():
            dpath = path.joinpath(i)
            if not dpath.exists():
                raise PreCheckFail(f"Path {dpath} does not exist")
            if not dpath.is_dir():
                raise PreCheckFail(f"Path {dpath} is not a directory")
        for i in cls.MK_MAINS:
            mfile = path.joinpath(i, "main.yaml")
            if not mfile.exists():
                raise PreCheckFail(f"file {i} does not exist")
