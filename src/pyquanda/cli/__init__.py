#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""common cli attributes."""
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from typing import Callable, Dict, List

from pyquanda.environment import REMOTE_BASE_PATH, INTERVIEW_CONFIG_REMOTE_FILE

from pyquanda.cli.templates import TYPES as _MAP


class ParserWrap:
    """ParserWrap."""

    def __init__(
        self, parser: ArgumentParser, description: str = None
    ) -> None:
        """__init__.

        Args:
            parser (ArgumentParser): parser
            description (str): description

        Returns:
            None:
        """
        parser.formatter_class = RawDescriptionHelpFormatter
        self.parser = parser
        if description:
            parser.description = description

    def add_arg_type(self):
        """add_arg_type."""
        self.parser.add_argument(
            "type",
            help="module type",
            choices=_MAP,
            type=str,
        )

    def add_arg_name(self):
        """add_arg_name."""
        self.parser.add_argument(
            "name",
            help="module name",
            type=str,
        )

    def add_arg_description(self):
        """add_arg_description."""
        self.parser.add_argument(
            "description",
            help="module name",
            type=str,
        )

    def add_destination_directory(self, required: bool, default: str = None):
        """add_destination_directory.

        Args:
            required (bool): required
            default (str): default
        """
        self.parser.add_argument(
            "--destination_directory",
            "-d",
            required=required,
            help="src_module_dir help",
            default=default,
            type=str,
        )

    def add_debug(self):
        """add_no_overwrite."""
        self.parser.add_argument(
            "--debug",
            action="store_true",
            help="debug output, do not execute",
            default=False,
        )

    def add_overwrite(self):
        """add_no_overwrite."""
        self.parser.add_argument(
            "--overwrite",
            action="store_true",
            help="automatically overwrite destination directory",
            default=False,
        )

    def add_src_module_directory(self):
        """add_src_module_directory."""
        if REMOTE_BASE_PATH.exists():
            req = False
            def_dir = REMOTE_BASE_PATH
        else:
            req = True
            def_dir = None

        self.parser.add_argument(
            "-s",
            "--src_module_dir",
            help="source module directory",
            required=req,
            default=def_dir,
            type=str,
        )

    def add_interview_config(self, required=False):
        """add_interview_config."""
        # explicitly required
        if required is False:
            req = False
            def_path = INTERVIEW_CONFIG_REMOTE_FILE
        elif required is True:
            if INTERVIEW_CONFIG_REMOTE_FILE.exists():
                req = False
                def_path = INTERVIEW_CONFIG_REMOTE_FILE
            else:
                req = True
                def_path = None
        # default to required
        else:
            req = True
            def_path = None

        self.parser.add_argument(
            "-c",
            "--interview_config_yaml",
            help="starting configuration yaml",
            required=req,
            default=def_path,
            type=str,
        )


class MainParser(ParserWrap):
    """MainParser."""

    ACTION_KEY = "action"

    def __init__(self, description: str) -> None:
        """__init__.

        Args:
            description (str): description

        Returns:
            None:
        """
        parser = ArgumentParser()
        super().__init__(parser, description)
        self.subparser = self.parser.add_subparsers(
            dest=self.ACTION_KEY, required=True
        )
        self.call_map = {}  # type: Dict[str, Callable]

    def add_subcommand(
        self, command: str, description: str, func: Callable
    ) -> ParserWrap:
        """add_subcommand.

        Args:
            command (str): command
            description (str): description
            func (Callable): func

        Returns:
            ParserWrap: parser wrap
        """
        sub = self.subparser.add_parser(command, help=description)
        self.call_map[command] = func
        return ParserWrap(sub, description)

    def display_subcommand_help(self, command: str):
        """display_subcommand_help.

        Args:
            command (str): command
        """
        parser = self.subparser.choices[command]  # type: ArgumentParser
        parser.print_help()

    def run(self, test_args: List = None):
        """run.

        Args:
            test_args (List): test_args

        Raises:
            SystemExit: if an error occures
        """
        args = self.parser.parse_args(test_args)
        tdict = dict(args.__dict__)
        action = tdict.pop("action")
        if not tdict:
            self.display_subcommand_help(action)
            raise SystemExit()
        func = self.call_map[args.action]
        func(args)
