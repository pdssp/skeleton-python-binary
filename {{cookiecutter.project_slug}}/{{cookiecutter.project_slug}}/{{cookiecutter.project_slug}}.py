import logging
import configparser

class {{cookiecutter.project_slug}}Lib:
    def __init__(self, path_to_conf: str, directory: str, *args, **kwargs):
        if "level" in kwargs:
            self._parse_level(kwargs["level"])

        self.__directory = directory
        self.__config = configparser.ConfigParser()
        self.__config.optionxform = str # type: ignore
        self.__config.read(path_to_conf)


    def _parse_level(self, level: str):
        """Parse level name and set the rigt level for the logger.
        If the level is not known, the INFO level is set

        Args:
            level (str): level name
        """
        logger = logging.getLogger()
        if level == "INFO":
            logger.setLevel(logging.INFO)
        elif level == "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif level == "WARNING":
            logger.setLevel(logging.WARNING)
        elif level == "ERROR":
            logger.setLevel(logging.ERROR)
        elif level == "CRITICAL":
            logger.setLevel(logging.CRITICAL)
        elif level == "TRACE":
            logger.setLevel(logging.TRACE) # type: ignore
        else:
            logger.warning(
                "Unknown level name : %s - setting level to INFO" % level
            )
            logger.setLevel(logging.INFO)

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