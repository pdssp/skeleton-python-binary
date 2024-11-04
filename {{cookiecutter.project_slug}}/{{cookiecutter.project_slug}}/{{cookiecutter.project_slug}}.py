# -*- coding: utf-8 -*-
# {{cookiecutter.project_name}} - {{cookiecutter.project_description}}
# Copyright (C) {{cookiecutter.year}} - {{cookiecutter.institute}} ({{cookiecutter.full_name}} for {{cookiecutter.consortium_name}})
# This file is part of {{cookiecutter.project_name}} <{{ cookiecutter.project_url }}>
# SPDX-License-Identifier: {% if cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}LGPL-3.0-or-later{% elif cookiecutter.open_source_license == 'Apache V2.0' -%}Apache-2.0{% elif cookiecutter.open_source_license == 'MIT' -%}MIT{% endif %}
"""This module contains the library."""
import sys
import configparser
from loguru import logger
from ._version import __name_soft__
from typing import Any
from typing import Dict

class {{cookiecutter.project_class_lib}}:
    """The library"""
    
    def __init__(self, **kwargs):
        # pylint: disable=unused-argument
        path_to_conf = kwargs.get("conf_file", "conf/testmyproject.conf")
        self.__config: configparser.ConfigParser = configparser.ConfigParser()
        self.__config.optionxform = str  # type: ignore
        self.__config.read(path_to_conf)
                
        self.__level: str = kwargs.get("level", 'INFO')        
        {{cookiecutter.project_class_lib}}._parse_level(self.__level)


    @staticmethod
    def _parse_level(level: str):
        """Parse level name and set the rigt level for the logger.
        If the level is not known, the INFO level is set

        Args:
            level (str): level name
        """
        if level == "INFO":
            loguru_level = "INFO"
        elif level == "DEBUG":
            loguru_level = "DEBUG"
        elif level == "WARNING":
            loguru_level = "WARNING"
        elif level == "ERROR":
            loguru_level = "ERROR"
        elif level == "CRITICAL":
            loguru_level = "CRITICAL"
        elif level == "TRACE":
            loguru_level = "TRACE"
        else:            
            loguru_level = "INFO"
            logger.log(loguru_level, f"Unknown level name : {level} - setting level to INFO")
            
        logger.remove()
        logger.add(sys.stdout, level=loguru_level)

    @property
    def config(self) -> configparser.ConfigParser:
        """The configuration file.

        :getter: Returns the configuration file
        :type: configparser.ConfigParser
        """
        return self.__config
    
    def run(self, *args, **kwargs):
        pass
