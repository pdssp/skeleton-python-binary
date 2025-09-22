# -*- coding: utf-8 -*-
import logging
import sys

import pytest
from loguru import logger

@pytest.fixture(autouse=True, scope="session")
def configure_logging(request):
    logger.remove()
    log_level = request.config.getoption("log_cli_level")
    if log_level is None:
        log_level = "INFO"
    logger.add(sys.stdout, level=log_level.upper())

class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Transfert vers logging Python standard
        logging.getLogger(record.name).handle(record)

def pytest_configure(config):
    logger.remove()
    log_level = config.getoption("log_cli_level")
    if log_level is None:
        log_level = "INFO"
    logger.add(InterceptHandler(), level=log_level.upper())

def pytest_collection_modifyitems(items):
    for item in items:
        # Ignorer les tests qui impliquent TestsVersion
        if "TestsVersion" in str(item.nodeid):
            item.add_marker(pytest.mark.skip(reason="TestsVersion is not a test case"))
