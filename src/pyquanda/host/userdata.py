#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Userdata / bootstrap module."""

import os
import shutil
import tempfile
import zipfile
from pathlib import Path

from pyquanda.environment import (
    INTERVIEW_CONFIG_REMOTE_FILE,
    REMOTE_BASE_PATH,
)
from pyquanda.exceptions import PreCheckFail
from pyquanda.host.main_intro_data import MainIntroCollection
from pyquanda.host.mods import ModuleLoader, ModulesCollection
from pyquanda.host.question_data import QuestionCollection


class UserDataScript:
    """UserDataScript."""

    def __init__(
        self,
        plugins_path: str,
        config_file: str,
        pkg_gzip: str = None,
    ):
        """__init__."""
        self.config_file = config_file
        self.plugins_path = Path(plugins_path)
        if pkg_gzip:
            _path = Path(pkg_gzip)
            if not _path.exists():
                raise PreCheckFail(f"{pkg_gzip} does not exist")
            self.pkg_gzip = _path
        else:
            self.pkg_gzip = None
        self._init_mods()
        self.basedir = Path("")
        self.tempdir = Path("")
        self._copy_dirs = []

    def _init_mods(self):
        """_init_mods."""
        # init modules
        for mod_path in self.plugins_path.iterdir():
            ModuleLoader.load(mod_path)

    @staticmethod
    def iter_network_ports():
        """iter_network_ports."""
        for i in ModulesCollection.network_ports():
            yield i

    def __enter__(self):
        """__enter__."""
        self.basedir = Path(tempfile.mkdtemp())
        self.tempdir = self.basedir.joinpath("staging")
        self._setup()
        return self

    def __exit__(self, *_):
        """__exit__.

        Args:
            _:
        """
        shutil.rmtree(self.basedir)

    @staticmethod
    def show_run_order():
        """show_run_order."""
        print("Run order:")
        for i in ModulesCollection.all():
            print(f"{i.order} {i.name}")

    def _setup(self):
        """_setup."""
        hook_dir = self.plugins_path.joinpath("_hooks")
        if hook_dir.exists() and hook_dir.is_dir():
            shutil.copytree(hook_dir, self.tempdir.joinpath(hook_dir.name))

        for i in ModulesCollection.all():
            shutil.copytree(i.path, self.tempdir.joinpath(i.path.name))

        if self.pkg_gzip:
            dstpkg = self.tempdir.joinpath(self.pkg_gzip.name)
            shutil.copy(self.pkg_gzip, dstpkg)

    def zipfile(self):
        """zipfile."""
        _zfile = self.basedir.joinpath("userdata.zip")
        with zipfile.ZipFile(_zfile, "w", zipfile.ZIP_DEFLATED) as zfile:
            zfile.write(
                self.config_file, arcname=str(INTERVIEW_CONFIG_REMOTE_FILE)
            )
            for root, _, files in os.walk(self.tempdir):
                for file in files:
                    base = Path(
                        root.replace(str(self.tempdir), str(REMOTE_BASE_PATH))
                    )
                    exist = Path(root).joinpath(file)
                    nfile = base.joinpath(exist.name)
                    zfile.write(os.path.join(root, file), arcname=nfile)
        return _zfile


def main():
    """Run main function."""
    with UserDataScript(
        os.environ["PYINTERVIEW_MODULES"],
        str(INTERVIEW_CONFIG_REMOTE_FILE),
    ) as udata:
        zfile = udata.zipfile()
        print(zfile)
        shutil.copy(zfile, "/tmp/test.zip")
        for proto, port in udata.iter_network_ports():
            print(proto, port)
    QuestionCollection.export()
    MainIntroCollection.export()


if __name__ == "__main__":
    main()
