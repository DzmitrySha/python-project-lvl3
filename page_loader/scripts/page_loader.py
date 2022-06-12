#!/usr/bin/env python
"""Page Loader Script."""

import os
import argparse
from page_loader.page_loader import download


def main():
    """Get start here."""
    parser = argparse.ArgumentParser(
        prog='page_loader',
        description="Downloads a page from the internet "
                    "to the specified folder.")
    parser.add_argument('source_path', type=str)
    parser.add_argument('-o', '--output',
                        default=os.getcwd())
    args = parser.parse_args()
    print(download(args.source_path, args.output))


if __name__ == '__main__':
    main()
