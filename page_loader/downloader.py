"""Image loader module."""


from page_loader.processes import (make_soup, make_dir_path, create_dir,
                                   make_html_file_path, write_html_file,
                                   write_files)

tags = {
    "img": "src",
    "link": "href",
    # "script": "src",
}


def page_download(url: str, temp_folder=""):
    """Downloads and saves html page
    with local resources
    to exist specified folder"""

    soup = make_soup(url)
    dir_path = make_dir_path(url, temp_folder)
    create_dir(dir_path)
    # находим, скачиваем и записываем ресурсы со страницы (по тегу и аттрибуту)
    for tag, attr in tags.items():
        write_files(soup, url, tag, attr, dir_path)

    html_file_path = make_html_file_path(url, temp_folder)
    write_html_file(soup, html_file_path)

    return html_file_path
