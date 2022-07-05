"""Image loader module."""


from page_loader.processes import (make_soup, make_dir_path,
                                   write_html_file, write_bin_files)


def page_download(url: str, temp_folder=""):
    """Downloads and saves html page with images to exist specified folder"""

    # создаем директорию для сохранения файлов
    dir_path = make_dir_path(url, temp_folder)
    # создаем объект Beautifulsoup
    soup = make_soup(url)
    # создаем объект Beautifulsoup
    write_bin_files(soup, url, "img", "src", dir_path)
    html_file_path = write_html_file(soup, url, temp_folder)

    return html_file_path
