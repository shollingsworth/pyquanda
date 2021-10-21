#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cli subcommands."""
import os
import argparse
import shutil
from pathlib import Path
import tempfile
from zipfile import ZipFile

from pyquanda.ansible import Ansible
from pyquanda.cli import MainParser
from pyquanda.cli.templates import copy_type
from pyquanda.host.mods import ModuleLoader
from pyquanda.hooks.registry import HookLoader
from pyquanda.environment import (
    QUESTIONS_DATA,
    REMOTE_BASE_PATH,
    INTERVIEW_STATE_REMOTE_FILE,
    INTERVIEW_CONFIG_REMOTE_FILE,
    MOCK_CONFIG,
    DEMO_DIR,
)
from pyquanda.exceptions import PreCheckFail
from pyquanda.host.question_data import QuestionCollection
from pyquanda.host.main_intro_data import MainIntroCollection
from pyquanda.host.userdata import UserDataScript

BASE_YAML = Path("/tmp/interview.yaml")


XONSH_FILE = Path("~/.xonshrc").expanduser()
XONSH_TXT = """
#!/usr/bin/env xonsh
# -*- coding: utf-8 -*-
import os
from pyquanda.host.xonsh import QuestionPrompt
os.environ['XONSH_STORE_STDOUT'] = "True"
os.environ['PAGER'] = "less -r"
QuestionPrompt()
""".lstrip()


def yesno(question: str) -> bool:
    """Simple Yes/No Function."""
    prompt = f"{question} ? (y/n): "
    ans = input(prompt).strip().lower()
    if ans not in ["y", "n"]:
        print(f"{ans} is invalid, please try again...")
        return yesno(question)
    if ans == "y":
        return True
    return False


class CreateNewModule:
    """CreateNewModule."""

    def __init__(self, parent: MainParser) -> None:
        """__init__.

        Args:
            parent (MainParser): parent

        Returns:
            None:
        """
        _pwrap = parent.add_subcommand(
            "new",
            "create a new module from templates",
            self.create_new_module,
        )
        _pwrap.add_arg_type()
        _pwrap.add_arg_name()
        _pwrap.add_arg_description()
        _pwrap.add_no_overwrite()
        _pwrap.add_destination_directory(default=".", required=True)
        self.parser = _pwrap.parser

    @staticmethod
    def create_new_module(args: argparse.Namespace):
        """Run main function."""
        try:
            dst = Path(args.destination_directory)
            copy_type(args.type, dst, args.name, args.description)
            print(f"{dst.absolute()} created!")
        except PreCheckFail as _e:
            raise SystemExit(_e) from _e


class RunModule:
    """RunModule."""

    def __init__(self, parent: MainParser) -> None:
        """__init__.

        Args:
            parent (MainParser): parent

        Returns:
            None:
        """
        super().__init__()
        _pwrap = parent.add_subcommand(
            "a_single",
            "run ansible on a single module based on path",
            self.run,
        )
        _pwrap.add_src_module_directory()
        self.parser = _pwrap.parser

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        """
        src = Path(args.src_module_dir)
        obj = Ansible(src)
        obj.run()


class RunAllModules:
    """RunAllModules."""

    def __init__(self, parent: MainParser) -> None:
        """__init__.

        Args:
            parent (MainParser): parent

        Returns:
            None:
        """
        super().__init__()
        _pwrap = parent.add_subcommand(
            "a_all",
            "run all ansible modules in path",
            self.run,
        )
        self.parser = _pwrap.parser
        _pwrap.add_src_module_directory()

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        """
        mod_path = Path(args.src_module_dir)
        collection = []
        for i in mod_path.iterdir():
            if not i.is_dir():
                continue
            ans = Ansible(i)
            collection.append(ans)

        for mod in collection:
            mod.run()


class AssembleQuestions:
    """AssembleQuestions."""

    def __init__(self, parent: MainParser) -> None:
        """__init__.

        Args:
            parent (MainParser): parent

        Returns:
            None:
        """
        super().__init__()
        _pwrap = parent.add_subcommand(
            "q_save",
            "convert questions to pyquanda questions config file",
            self.run,
        )
        _pwrap.add_src_module_directory()
        _pwrap.add_destination_directory(
            required=False, default=str(QUESTIONS_DATA.parent)
        )
        self.parser = _pwrap.parser

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        """
        base_mod_path = Path(args.src_module_dir)
        for mod_path in base_mod_path.iterdir():
            if not mod_path.is_dir():
                continue
            ModuleLoader.load(mod_path)
        HookLoader.load()
        QuestionCollection.export()
        MainIntroCollection.export()


class TestQuestions:
    """TestQuestions."""

    def __init__(self, parent: MainParser) -> None:
        """__init__.

        Args:
            parent (MainParser): parent

        Returns:
            None:
        """
        _pwrap = parent.add_subcommand(
            "q_test",
            "test question set",
            self.run,
        )
        _pwrap.add_src_module_directory()
        self.parser = _pwrap.parser
        self.parser.add_argument(
            "--keep_state",
            "-k",
            action="store_true",
            help="keep state (defaults to False)",
            default=False,
        )

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args

        Raises:
            SystemExit: if there is an issue
        """
        args.destination_directory = QUESTIONS_DATA.parent
        AssembleQuestions.run(args)
        if not XONSH_FILE.exists():
            if not yesno(
                f"{XONSH_FILE} doesn't exist, would you like to create it?"
            ):
                raise SystemExit("Bye!")
            XONSH_FILE.write_text(XONSH_TXT)
        if INTERVIEW_STATE_REMOTE_FILE.exists() and not args.keep_state:
            INTERVIEW_STATE_REMOTE_FILE.unlink()
        os.system("xonsh")


class Demo:
    """Demo."""

    def __init__(self, parent: MainParser) -> None:
        """__init__.

        Args:
            parent (MainParser): parent

        Returns:
            None:
        """
        _pwrap = parent.add_subcommand(
            "demo",
            "demonstrate the xonsh question environment",
            self.run,
        )
        parser = _pwrap.parser
        parser.add_argument("--hidden", help=argparse.SUPPRESS, default=None)

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        """
        if INTERVIEW_STATE_REMOTE_FILE.exists():
            INTERVIEW_STATE_REMOTE_FILE.unlink()
        INTERVIEW_CONFIG_REMOTE_FILE.write_text(MOCK_CONFIG)
        args.destination_directory = QUESTIONS_DATA.parent
        args.src_module_dir = DEMO_DIR
        AssembleQuestions.run(args)
        with tempfile.TemporaryDirectory() as tdir:
            tempdir = Path(tdir)
            xonrc = tempdir.joinpath("xonshrc")
            xonrc.write_text(XONSH_TXT)
            os.system(f"xonsh --rc {xonrc}")


class SaveUserData:
    """SaveUserData."""

    def __init__(self, parent: MainParser) -> None:
        """__init__.

        Args:
            parent (MainParser): parent

        Returns:
            None:
        """
        super().__init__()
        _pwrap = parent.add_subcommand(
            "userdata",
            "save userdata zip file in directory (filename: userdata.zip)",
            self.run,
        )
        _pwrap.add_src_module_directory()
        _pwrap.add_destination_directory(required=True)
        self.parser = _pwrap.parser

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        """
        with UserDataScript(args.src_module_dir) as udata:
            dest_dir = Path(args.destination_directory)
            zfile = udata.zipfile()
            dest_file = dest_dir.joinpath(zfile.name)
            shutil.copy(zfile, dest_file)

            print(f"{dest_file.absolute()} saved!")


class Bootstrap:
    """Bootstrap."""

    def __init__(self, parent: MainParser) -> None:
        """__init__.

        Args:
            parent (MainParser): parent

        Returns:
            None:
        """
        super().__init__()
        _pwrap = parent.add_subcommand(
            "bootstrap",
            "bootstrap host given userdata.zip file",
            self.run,
        )
        self.parser = _pwrap.parser
        self.parser.add_argument(
            "userdata_file",
            type=str,
        )

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        Raises:
            SystemExit: on error
        """
        pzip = Path(args.userdata_file)
        if not pzip.exists():
            raise SystemExit(f"{pzip} file does not exist")
        with ZipFile(pzip, "r") as zip_ref:
            zip_ref.extractall("/")

        ns = argparse.Namespace()
        ns.src_module_dir = str(REMOTE_BASE_PATH)
        AssembleQuestions.run(ns)
        RunAllModules.run(ns)
        pzip.unlink()
        shutil.rmtree(REMOTE_BASE_PATH)
        tmpdir = Path("/tmp")
        for i in tmpdir.iterdir():
            if i.name.startswith("tmp"):
                shutil.rmtree(i)
