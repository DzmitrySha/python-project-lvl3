"""Logging module"""

import logging

FORMAT = "(%(asctime)s) [%(levelname)s]: " \
         "%(name)s:%(filename)s:%(lineno)d %(message)s"

logging.basicConfig(
    format=FORMAT,
    filename='page_loader.log',
    filemode='w',
)


def make_logger(name):
    """Make logger"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
