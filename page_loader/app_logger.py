"""Logging module"""

import os
import logging
from page_loader.processes import create_dir

_log_file_format = "%(asctime)s [%(levelname)s]: " \
                   "(%(filename)s) - %(funcName)s(%(lineno)d) - %(message)s"
_log_stream_format = "[%(levelname)s]: %(message)s"


def get_file_handler():
    create_dir(os.path.join(os.getcwd(), 'logs'))
    file_handler = logging.FileHandler("logs/app_log.log")
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(_log_file_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_stream_format))
    return stream_handler


def get_file_test_handler():
    create_dir(os.path.join(os.getcwd(), 'logs'))
    file_handler = logging.FileHandler("logs/test_logs.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_file_format))
    return file_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_stream_handler())
    logger.addHandler(get_file_handler())
    return logger


def get_test_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_test_handler())
    return logger
