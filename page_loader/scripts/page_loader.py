#!/usr/bin/env python
"""Page Loader Script."""
import sys

from page_loader.downloader import download
from page_loader.cli import parse_args_
from page_loader.app_logger import get_logger


logger = get_logger(__name__)


def main():
    """Get start here."""
    source_url, output = parse_args_()
    try:
        download(source_url, output)
    except Exception as error:
        logger.debug(error)
        logger.error(error)
        sys.exit(2)


if __name__ == '__main__':
    main()
