"""Logging module"""

import logging

_log_file_format = "%(asctime)s [%(levelname)s]: " \
                   "(%(filename)s) - %(funcName)s(%(lineno)d) - %(message)s"
_log_stream_format = "[%(levelname)s]: (%(filename)s.%(funcName)s): %(message)s"


def get_file_handler():
    """Make file handler"""
    file_handler = logging.FileHandler("app_log.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(_log_file_format))
    return file_handler


def get_stream_handler():
    """Make stream handler"""
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_stream_format))
    return stream_handler


def get_logger(name):
    """Make logger"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
