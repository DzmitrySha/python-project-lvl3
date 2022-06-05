# Downloader

import requests


def download(source_path: str, temp_path='var/tmp'):
    r = requests.get(source_path)
    return r.text
