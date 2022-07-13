"""Page downloader module."""


from page_loader.processes import (make_soup, make_name,
                                   make_dir_path, create_dir,
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

    html_file_name = make_name(url, ".html")
    html_file_path = make_html_file_path(html_file_name, temp_folder)
    html_content = soup.prettify()
    write_html_file(html_file_path, html_content)

    return html_file_path
