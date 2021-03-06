#!/usr/bin/env python
"""Page Loader Script."""

from page_loader.downloader import page_download
from page_loader.cli import parse_args_


def main():
    """Get start here."""
    source_url, output = parse_args_()
    page_download(source_url, output)


if __name__ == '__main__':
    main()
