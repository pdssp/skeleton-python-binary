# {{cookiecutter.project_name}} - {{cookiecutter.project_short_description}}
# Copyright (C) {{cookiecutter.year}} - {{cookiecutter.institute}} ({{cookiecutter.full_name}} for {{cookiecutter.consortium_name}})
#
# This file is part of {{cookiecutter.project_name}}.
#
# {{cookiecutter.project_name}} is free software: you can redistribute it and/or modify
# it under the terms of the {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License v3 {% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License v3{% endif %} as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# {{cookiecutter.project_name}} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License v3 {% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License v3{% endif %} for more details.
#
# You should have received a copy of the {% if cookiecutter.open_source_license == 'GNU General Public License v3' -%}GNU General Public License{% elif cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}GNU Lesser General Public License v3 {% elif cookiecutter.open_source_license == 'GNU Affero General Public License v3' -%}GNU Affero General Public License v3{% endif %}
# along with {{cookiecutter.project_name}}.  If not, see <https://www.gnu.org/licenses/>.
"""Main program."""
import logging
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
        return argparse.HelpFormatter._split_lines(self, text, width)


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
        logging.error("You pressed Ctrl+C")
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
        "--output_directory",
        default="{{cookiecutter.project_slug}}-data",
        help="The output directory where the data products are created (default: %(default)s)",
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
    logger = logging.getLogger(__name__)
    handler = SigintHandler()
    signal.signal(signal.SIGINT, handler.signal_handler)
    try:
        options_cli = parse_cli()

        {{cookiecutter.project_slug}} = {{cookiecutter.project_class_lib}}(
            options_cli.conf_file,
            options_cli.output_directory,
            level=options_cli.level,
        )
        logger.info({{cookiecutter.project_slug}})
        sys.exit(0)
    except Exception as error:  # pylint: disable=broad-except
        logging.exception(error)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    # execute only if run as a script
    run()
