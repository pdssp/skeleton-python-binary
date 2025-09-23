# -*- coding: utf-8 -*-
# {{cookiecutter.project_name}} - {{cookiecutter.project_description}}
# Copyright (C) {{cookiecutter.year}} - {{cookiecutter.institute}} ({{cookiecutter.full_name}} for {{cookiecutter.consortium_name}})
# This file is part of {{cookiecutter.project_name}} <{{ cookiecutter.project_url }}>
# SPDX-License-Identifier: {% if cookiecutter.open_source_license == 'GNU Lesser General Public License v3' -%}LGPL-3.0-or-later{% elif cookiecutter.open_source_license == 'Apache V2.0' -%}Apache-2.0{% elif cookiecutter.open_source_license == 'MIT' -%}MIT{% endif %}
"""This module contains the library."""
import configparser
from .config import configure_logging
from loguru import logger

class {{cookiecutter.project_class_lib}}:
    """The library"""

    def __init__(self, **kwargs):
        # pylint: disable=unused-argument
        configure_logging(level=kwargs.get("level"))        
        path_to_conf = kwargs.get("conf_file", "conf/testmyproject.conf")
        self.__config: configparser.ConfigParser = configparser.ConfigParser()
        self.__config.optionxform = str  # type: ignore
        self.__config.read(path_to_conf)

    @property
    def config(self) -> configparser.ConfigParser:
        """The configuration file.

        :getter: Returns the configuration file
        :type: configparser.ConfigParser
        """
        return self.__confi

    def run(self, **kwargs):
        pass
