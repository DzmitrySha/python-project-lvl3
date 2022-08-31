"""Parsing args from command line."""

import os
import argparse


def parse_args_():
    parser = argparse.ArgumentParser(
        prog='page_loader',
        description="Downloads a page from the internet "
                    "to the specified folder.")
    parser.add_argument('source_url', type=str)
    parser.add_argument('-o', '--output', default=os.getcwd())
    args = parser.parse_args()
    return args.source_url, args.output
