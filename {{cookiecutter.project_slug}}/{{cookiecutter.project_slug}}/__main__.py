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
from {{cookiecutter.project_slug}} import __name_soft__
from {{cookiecutter.project_slug}} import __author__
from {{cookiecutter.project_slug}} import __copyright__
from {{cookiecutter.project_slug}} import __description__
from {{cookiecutter.project_slug}} import __version__
from .{{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}Lib


class SmartFormatter(argparse.HelpFormatter):
    def _split_lines(self, text, width):
        if text.startswith("R|"):
            return text[2:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)


class SIGINT_handler:
    def __init__(self):
        self.SIGINT = False

    def signal_handler(self, signal, frame):
        logging.error("You pressed Ctrl+C")
        self.SIGINT = True
        sys.exit(2)

def str2bool(v: str) -> bool:
    return v.lower() in ("yes", "true", "True", "t", "1")

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
    logger = logging.getLogger(__name__)
    logger.info(f"Main program of {__name_soft__}")
    handler = SIGINT_handler()
    signal.signal(signal.SIGINT, handler.signal_handler)
    try:
        options_cli = parse_cli()

        {{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}Lib(
            options_cli.conf_file,
            options_cli.output_directory,
            level=options_cli.level,
        )
        logger.info({{cookiecutter.project_slug}})
        sys.exit(0)
    except Exception as e:
        logging.exception(e)
        sys.exit(1)
    print("OK")

if __name__ == "__main__":
    # execute only if run as a script
    run()
