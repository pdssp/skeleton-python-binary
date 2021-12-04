import logging

#import numpy as np
import pytest
import {{cookiecutter.project_slug}}
#from PIL import Image


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
