"""IMG downloader module."""

# from page_loader.processes import (make_soup, make_name, make_dir_path,
#                                    make_html_file_path,
#                                    create_dir, write_bin_file)
#
# TAGS = {
#     "img": "src",
#     "link": "href",
#     # "script": "src",
# }
#
#
# def sources_download(url: str, temp_folder=''):
#     soup = make_soup(url)
#     dir_name = make_name(url, ext="_files")
#     dir_path = make_dir_path(dir_name, temp_folder)
#     create_dir(dir_path)
#
#
#     for tag, attr in TAGS.items():
#         list_tags = soup.find_all(tag)
#         file_content = get_content(soup, tag, attr)
#         file_path = make_html_file_path(html_file_name, temp_folder)
#
#         write_file(file_path, file_content)
#     pass
#
#
# def get_content(url: str, tag: str, attr: str,):
#     # доменное имя
#     domain_name = urlparse(url).netloc
#     # собираем список строк с тегами tags из объекта soup
#     list_tags = soup.find_all(tag)
#     for line in list_tags:
#         # для каждой строки из списка берём значение его аттрибута
#         line_url = clearing_url(line.get(attr))
#         line_domain_name = urlparse(line_url).netloc
#
#         if domain_name in line_domain_name or not line_domain_name:
#             if not line_domain_name:
#                 line_url = urljoin(url, line_url)
#             source_name = make_name(line_url, os.path.splitext(line_url)[1])
#             local_path = os.path.join(dir_path, source_name)
#             content = requests.get(line_url).content
#
#             write_bin_file(local_path, content)
#
#             # заменяем ссылки на локальные пути к файлам
#             for source in list_tags:
#                 source[attr] = source[attr].replace(line_url, local_path)
