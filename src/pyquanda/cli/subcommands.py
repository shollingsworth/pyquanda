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
    InterviewConfig,
)
from pyquanda.exceptions import PreCheckFail
from pyquanda.host.question_data import QuestionCollection
from pyquanda.host.main_intro_data import MainIntroCollection
from pyquanda.host.userdata import UserDataScript


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


def _config_replace_if_arg_given(src_config: str):
    """If defined in an argument, replace the the default runtime with the given path."""
    path = Path(src_config)
    if path == INTERVIEW_CONFIG_REMOTE_FILE:
        return
    if not path.exists():
        raise PreCheckFail(f"{path} does not exist")
    # kick the file to make sure it's valid
    shutil.copy(src_config, INTERVIEW_CONFIG_REMOTE_FILE)
    InterviewConfig().as_dict()


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
        _pwrap.add_overwrite()
        _pwrap.add_destination_directory(default=".", required=True)
        self.parser = _pwrap.parser

    @staticmethod
    def create_new_module(args: argparse.Namespace):
        """Run main function."""
        dst = Path(args.destination_directory)
        copy_type(args.type, dst, args.name, args.description)
        print(f"{dst.absolute()} created!")


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
        _pwrap.add_interview_config()
        _pwrap.add_src_module_directory()
        _pwrap.add_debug()
        self.parser = _pwrap.parser

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        """
        src = Path(args.src_module_dir)
        if args.interview_config_yaml:
            _config_replace_if_arg_given(args.interview_config_yaml)
        Ansible.run_single(src, args.debug)


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
        _pwrap.add_interview_config()
        _pwrap.add_src_module_directory()
        _pwrap.add_debug()

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        """
        if args.interview_config_yaml:
            _config_replace_if_arg_given(args.interview_config_yaml)
        mod_path = Path(args.src_module_dir)
        Ansible.run_all(mod_path, args.debug)


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
        _pwrap.add_interview_config()
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
        if args.interview_config_yaml:
            _config_replace_if_arg_given(args.interview_config_yaml)
        base_mod_path = Path(args.src_module_dir)
        for mod_path in base_mod_path.iterdir():
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
        _pwrap.add_interview_config()
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
        if args.interview_config_yaml:
            _config_replace_if_arg_given(args.interview_config_yaml)
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
        _pwrap.add_destination_directory(required=False)
        _pwrap.add_overwrite()
        parser.add_argument("--hidden", help=argparse.SUPPRESS, default=None)

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        """
        INTERVIEW_CONFIG_REMOTE_FILE.write_text(MOCK_CONFIG)
        if INTERVIEW_STATE_REMOTE_FILE.exists():
            INTERVIEW_STATE_REMOTE_FILE.unlink()
        args.destination_directory = QUESTIONS_DATA.parent
        args.src_module_dir = DEMO_DIR
        args.interview_config_yaml = INTERVIEW_CONFIG_REMOTE_FILE
        AssembleQuestions.run(args)
        with tempfile.TemporaryDirectory() as tdir:
            tempdir = Path(tdir)
            shutil.copytree(args.src_module_dir, tempdir.joinpath("modules"))
            shutil.copy(
                args.interview_config_yaml,
                tempdir.joinpath(args.interview_config_yaml.name),
            )
            xonrc = tempdir.joinpath("xonshrc")
            xonrc.write_text(XONSH_TXT)
            xonsh_cmd = f"xonsh --rc {xonrc}"
            os.system(xonsh_cmd)
            ddir = args.destination_directory.joinpath(
                "pyquanda_demo"
            ).absolute()
            save_msg = [
                "Edit / run this again with",
                f"pyquanda-cmd q_test -s {ddir}/modules -c"
                f" {ddir}/interview.yaml",
            ]
            if ddir.exists():
                if not args.overwrite:
                    print(
                        f"{args.destination_directory} exists, set"
                        " --overwrite if you would like to overwrite"
                    )
                    return
                shutil.rmtree(ddir)
            shutil.copytree(tempdir, ddir)
            print(f"Demo saved to: {ddir}")
            print("\n".join(save_msg))


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
        _pwrap.add_interview_config(required=True)
        _pwrap.add_src_module_directory()
        _pwrap.add_destination_directory(required=True)
        self.parser = _pwrap.parser

    @staticmethod
    def run(args: argparse.Namespace):
        """run.

        Args:
            args (argparse.Namespace): args
        """
        with UserDataScript(
            args.src_module_dir, args.interview_config_yaml
        ) as udata:
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
        ns.interview_config_yaml = str(INTERVIEW_CONFIG_REMOTE_FILE)
        ns.debug = False
        AssembleQuestions.run(ns)
        RunAllModules.run(ns)
        pzip.unlink()
        for i in REMOTE_BASE_PATH.iterdir():
            if i.name == "_hooks":
                continue
            shutil.rmtree(i)
        tmpdir = Path("/tmp")
        for i in tmpdir.iterdir():
            if i.name.startswith("tmp"):
                shutil.rmtree(i)
