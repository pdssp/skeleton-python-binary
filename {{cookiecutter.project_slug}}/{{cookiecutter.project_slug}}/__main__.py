# -*- coding: utf-8 -*-
# {{cookiecutter.project_name}} - {{cookiecutter.project_description}}
# Copyright (C) {{cookiecutter.year}} - {{cookiecutter.institute}} ({{cookiecutter.full_name}} for {{cookiecutter.consortium_name}})
# This file is part of {{cookiecutter.project_name}} <{{ cookiecutter.project_url }}>
# SPDX-License-Identifier: {% if cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}LGPL-3.0-or-later{% elif cookiecutter.open_source_license == 'Apache V2.0' -%}Apache-2.0{% elif cookiecutter.open_source_license == 'MIT' -%}MIT{% endif %}
"""Main program."""
from loguru import logger
import argparse
import signal
import sys
from {{cookiecutter.project_slug}} import __author__
from {{cookiecutter.project_slug}} import __copyright__
from {{cookiecutter.project_slug}} import __description__
from {{cookiecutter.project_slug}} import __version__
from .{{cookiecutter.project_slug}} import {{cookiecutter.project_class_lib}}


class SmartFormatter(argparse.HelpFormatter):
    """Smart formatter for argparse - The lines are split for long text"""

    def _split_lines(self, text, width):
        if text.startswith("R|"):
            return text[2:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(  # pylint: disable=protected-access
            self, text, width
        )


class SigintHandler:  # pylint: disable=too-few-public-methods
    """Handles the signal"""

    def __init__(self):
        self.SIGINT = False   # pylint: disable=invalid-name

    def signal_handler(self, sig: int, frame):
        """Trap the signal

        Args:
            sig (int): the signal number
            frame: the current stack frame
        """
        # pylint: disable=unused-argument
        logger.error("You pressed Ctrl+C")
        self.SIGINT = True
        sys.exit(2)


def str2bool(string_to_test: str) -> bool:
    """Checks if a given string is a boolean

    Args:
        string_to_test (str): string to test

    Returns:
        bool: True when the string is a boolean otherwise False
    """
    return string_to_test.lower() in ("yes", "true", "True", "t", "1")


def parse_cli() -> argparse.Namespace:
    """Parse command line inputs.

    Returns
    -------
    argparse.Namespace
        Command line options
    """
    parser = argparse.ArgumentParser(
        description=__description__,
        formatter_class=SmartFormatter,
        epilog=__author__ + " - " + __copyright__,
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s " + __version__
    )

    parser.add_argument(
        "--conf_file",
        default="conf/{{cookiecutter.project_slug}}.conf",
        help="The location of the configuration file (default: %(default)s)",
    )
    
    parser.add_argument(
        "--directory",
        default="/app",
        help="The base directory where the data products are read and saved (default: %(default)s)",
    )

    parser.add_argument(
        "--level",
        choices=[
            "INFO",
            "DEBUG",
            "WARNING",
            "ERROR",
            "CRITICAL",
            "TRACE",
        ],
        default="INFO",
        help="set Level log (default: %(default)s)",
    )

    return parser.parse_args()


def run():
    """Main function that instanciates the library."""
    handler = SigintHandler()
    signal.signal(signal.SIGINT, handler.signal_handler)
    try:
        options_cli = parse_cli()

        {{cookiecutter.project_slug}} = {{cookiecutter.project_class_lib}}(
            **vars(options_cli)
        )
        {{cookiecutter.project_slug}}.run()
        sys.exit(0)
    except Exception as error:  # pylint: disable=broad-except
        logger.exception(error)
        sys.exit(1)


if __name__ == "__main__":
    # execute only if run as a script
    run()
