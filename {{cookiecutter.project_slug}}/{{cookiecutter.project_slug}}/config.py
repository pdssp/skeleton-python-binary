from loguru import logger
import sys

# ---- Logging configuration ----
def configure_logging(level="INFO", sink=sys.stderr, **kwargs):
    """
    Configure a global loguru logger.
    """
    logger.remove()
    logger.add(sink, level=level.upper(), **kwargs)
