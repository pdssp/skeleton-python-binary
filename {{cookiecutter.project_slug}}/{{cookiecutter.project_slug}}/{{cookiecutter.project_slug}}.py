"""This module contains the library."""
import logging
import configparser
from ._version import __name_soft__

logger = logging.getLogger(__name__)


class {{cookiecutter.project_class_lib}}:
    """The library"""

    def __init__(self, path_to_conf: str, directory: str, *args, **kwargs):
        # pylint: disable=unused-argument
        if "level" in kwargs:
            {{cookiecutter.project_class_lib}}._parse_level(kwargs["level"])

        self.__directory = directory
        self.__config = configparser.ConfigParser()
        self.__config.optionxform = str  # type: ignore
        self.__config.read(path_to_conf)

    @staticmethod
    def _parse_level(level: str):
        """Parse level name and set the rigt level for the logger.
        If the level is not known, the INFO level is set

        Args:
            level (str): level name
        """
        logger_main = logging.getLogger(__name_soft__)
        if level == "INFO":
            logger_main.setLevel(logging.INFO)
        elif level == "DEBUG":
            logger_main.setLevel(logging.DEBUG)
        elif level == "WARNING":
            logger_main.setLevel(logging.WARNING)
        elif level == "ERROR":
            logger_main.setLevel(logging.ERROR)
        elif level == "CRITICAL":
            logger_main.setLevel(logging.CRITICAL)
        elif level == "TRACE":
            logger_main.setLevel(logging.TRACE)  # type: ignore # pylint: disable=no-member
        else:
            logger_main.warning(
                "Unknown level name : %s - setting level to INFO", level
            )
            logger_main.setLevel(logging.INFO)

    @property
    def config(self) -> configparser.ConfigParser:
        """The configuration file.

        :getter: Returns the configuration file
        :type: configparser.ConfigParser
        """
        return self.__config

    @property
    def directory(self) -> str:
        """The output directory.

        :getter: Returns the output directory
        :type: str
        """
        return self.__directory
