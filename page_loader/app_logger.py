"""Logging module"""

import logging


class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s " \
    #          "(%(filename)s:%(lineno)d)"

    _file_format = "(%(asctime)s) [%(levelname)s]: " \
                   "%(name)s:%(filename)s:%(lineno)d %(message)s"

    _stream_format = "[%(levelname)s] %(message)s"

    FORMATS = {
        logging.DEBUG: grey + _file_format + reset,
        logging.INFO: grey + _stream_format + reset,
        logging.WARNING: yellow + _file_format + reset,
        logging.ERROR: red + _stream_format + reset,
        logging.CRITICAL: bold_red + _file_format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(name):
    """Make logger"""
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(CustomFormatter())
    #
    with open('page_loader.log', 'w'):
        pass
    file_handler = logging.FileHandler("page_loader.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(CustomFormatter())

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
