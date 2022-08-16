"""Logging module"""

import logging


FORMAT = "(%(asctime)s) [%(levelname)s]: " \
         "%(name)s:%(filename)s:%(lineno)d %(message)s"

logging.basicConfig(
    format=FORMAT,
    filename="page_loader.log"
)


def get_logger(name):
    """Make logger"""
    with open('page_loader.log', 'w'):
        pass
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
