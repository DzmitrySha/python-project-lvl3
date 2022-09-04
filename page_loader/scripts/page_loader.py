#!/usr/bin/env python
"""Page Loader Script."""
import os
import sys
from page_loader.downloader import download
from page_loader.cli import parse_args_
from page_loader.app_logger import make_logger

logger = make_logger(__name__)


def main():
    """Get start here."""
    source_url, output = parse_args_()
    output_path = os.path.join(os.getcwd(), output)
    print(f"Requested url: {source_url}")
    print(f"Output folder: {output_path}")

    try:
        output_path = download(source_url, output)
        print(f"Page was downloaded as: {output_path}")
    except Exception as error:
        logger.debug(error)
        print("An unexpected error occurred. "
              "See log file for details (page_loader.log).")
        sys.exit(1)


if __name__ == '__main__':
    main()
