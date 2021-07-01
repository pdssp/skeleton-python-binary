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
"""Module for customizing ths logs."""
import logging
from typing import Optional


class UtilsLogs:  # pylint: disable=R0903
    """Utility class for logs."""

    @staticmethod
    def add_logging_level(
        level_name: str, level_num: int, method_name: Optional[str] = None
    ) -> None:
        """Add a new logging level to the `logging` module.

        Parameters
        ----------
        level_name: str
            level name of the logging
        level_num: int
            level number related to the level name
        method_name: Optional[str]
            method for both `logging` itself and the class returned by
            `logging.Logger`

        Returns
        -------
            None

        Raises
        ------
        AttributeError
            If this levelName or methodName is already defined in the
            logger.

        """
        if not method_name:
            method_name = level_name.lower()

        def log_for_level(self, message, *args, **kwargs):
            if self.isEnabledFor(level_num):
                self._log(  # pylint: disable=W0212
                    level_num, message, args, **kwargs
                )

        def log_to_root(message, *args, **kwargs):
            logging.log(level_num, message, *args, **kwargs)

        logging.addLevelName(level_num, level_name)
        setattr(logging, level_name, level_num)
        setattr(logging.getLoggerClass(), method_name, log_for_level)
        setattr(logging, method_name, log_to_root)


class LogRecord(logging.LogRecord):  # pylint: disable=R0903
    """Specific class to handle output in logs."""

    def getMessage(self) -> str:
        """Returns the message.

        Format the message according to the type of the message.

        Returns:
            str: Returns the message
        """
        msg = str(self.msg)
        if isinstance(self.args, dict):
            return msg.format(self.args)
        return msg.format(*self.args) if self.args else msg


class CustomColorFormatter(logging.Formatter):
    """Color formatter."""

    UtilsLogs.add_logging_level("TRACE", 15)
    # Reset
    color_Off = "\033[0m"  # Text Reset

    log_colors = {
        logging.TRACE: "\033[0;36m",  # type: ignore # pylint: disable=no-member # cyan
        logging.DEBUG: "\033[1;34m",  # blue
        logging.INFO: "\033[0;32m",  # green
        logging.WARNING: "\033[1;33m",  # yellow
        logging.ERROR: "\033[1;31m",  # red
        logging.CRITICAL: "\033[1;41m",  # red reverted
    }

    def format(self, record) -> str:
        """Format the log.

        Args:
            record: the log record

        Returns:
            str: the formatted log record
        """
        record.levelname = "{}{}{}".format(
            CustomColorFormatter.log_colors[record.levelno],
            record.levelname,
            CustomColorFormatter.color_Off,
        )
        record.msg = "{}{}{}".format(
            CustomColorFormatter.log_colors[record.levelno],
            record.msg,
            CustomColorFormatter.color_Off,
        )

        # Select the formatter according to the log if several handlers are
        # attached to the logger
        my_formatter = logging.Formatter
        my_handler = None
        handlers = logging.getLogger(__name__).handlers
        for handler in handlers:
            handler_level = handler.level
            if (
                handler_level
                == logging.getLogger(__name__).getEffectiveLevel()
            ):
                if handler.formatter:
                    my_formatter._fmt = (  # pylint: disable=W0212
                        handler.formatter._fmt  # pylint: disable=W0212
                    )
                my_handler = handler
                break
        if my_handler is not None:
            for handler in handlers:
                if handler != my_handler:
                    logging.getLogger(__name__).removeHandler(handler)
        return my_formatter.format(self, record)  # type: ignore


class ShellColorFormatter(CustomColorFormatter):
    """Shell Color formatter."""

    def format(self, record) -> str:
        """Format the log.

        Args:
            record: the log record

        Returns:
            str: the formatted log record
        """
        record.msg = "{}{}{}".format(
            CustomColorFormatter.log_colors[logging.INFO],
            record.msg,
            CustomColorFormatter.color_Off,
        )
        return record.msg
