import logging

#import numpy as np
import pytest
import {{cookiecutter.project_slug}}
#from PIL import Image

logger = logging.getLogger(__name__)

@pytest.fixture
def setup():
    logger.info("----- Init the tests ------")


def test_init_setup(setup):
    logger.info("Setup is initialized")


# def assert_images_equal(image_1: str, image_2: str):
#     img1 = Image.open(image_1)
#     img2 = Image.open(image_2)

#     # Convert to same mode and size for comparison
#     img2 = img2.convert(img1.mode)
#     img2 = img2.resize(img1.size)

#     diff = np.asarray(img1).astype("float") - np.asarray(img2).astype("float")

#     sum_sq_diff = np.sum(diff ** 2)  # type: ignore

#     if sum_sq_diff == 0:
#         # Images are exactly the same
#         pass
#     else:
#         normalized_sum_sq_diff = sum_sq_diff / np.sqrt(sum_sq_diff)
#         assert normalized_sum_sq_diff < 0.001

def test_name():
    name = {{cookiecutter.project_slug}}.__name_soft__
    assert name == "{{cookiecutter.project_slug}}"

def test_logger():
    loggers = [logging.getLogger()]
    loggers = loggers + [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    assert loggers[0].name == "root"

def test_new_level():
    {{cookiecutter.project_slug}}.custom_logging.UtilsLogs.add_logging_level("TRACE", 20)
    logger = logging.getLogger("__main__")
    logger.setLevel(logging.TRACE)  # type: ignore
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.trace("Test the logger")  # type: ignore
    logger.log(logging.TRACE, "test")  # type: ignore


def test_message():
    record = {{cookiecutter.project_slug}}.custom_logging.LogRecord(
        "__main__",
        logging.INFO,
        "pathname",
        2,
        "message {val1} {val2}",
        {"val1": 10, "val2": "test"},
        None,
    )
    assert "message 10 test", record.getMessage()

    record = {{cookiecutter.project_slug}}.custom_logging.LogRecord(
        "__main__",
        logging.INFO,
        "pathname",
        2,
        "message {0} {1}",
        ("val1", "val2"),
        None,
    )
    assert "message val1 val2", record.getMessage()


def test_color_formatter():
    formatter = {{cookiecutter.project_slug}}.custom_logging.CustomColorFormatter()
    logger = logging.getLogger("{{cookiecutter.project_slug}}.custom_logging")
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)
    logger.addHandler(logging.NullHandler())
    logger.info("test")

    shell_formatter = {{cookiecutter.project_slug}}.custom_logging.ShellColorFormatter()
    record = {{cookiecutter.project_slug}}.custom_logging.LogRecord(
        "__main__",
        logging.INFO,
        "pathname",
        2,
        "message {0} {1}",
        ("val1", "val2"),
        None,
    )
    shell_formatter.format(record)