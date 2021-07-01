import pytest

import {{cookiecutter.project_slug}}
import logging

def test_name():
    name = {{cookiecutter.project_slug}}.__name_soft__
    assert name == "{{cookiecutter.project_slug}}"

def test_logger():
    loggers = [logging.getLogger()]
    loggers = loggers + [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    assert loggers[0].name == "root"
    assert loggers[1].name == "{{cookiecutter.project_slug}}"