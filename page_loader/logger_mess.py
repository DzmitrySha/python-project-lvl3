#
#
#
# if is_url_correct(url):
#     try:
#         requests.get(url)
#     except requests.exceptions.RequestException as error:
#         logger.error('requested url is not correct!')
#     # except (requests.exceptions.MissingSchema,
#     #         requests.exceptions.InvalidSchema,
#     #         requests.exceptions.InvalidURL,
#     #         requests.exceptions.HTTPError,
#     #         requests.exceptions.ConnectionError
#     #         ):
#         raise error
#
#
#
#     try:
#         is_folder_exists(temp_folder)
#     except OSError as error:
#         logger.info('the output folder does not exist!')
#         raise error

# class CustomFormatter(logging.Formatter):
#
#     grey = "\x1b[38;20m"
#     yellow = "\x1b[33;20m"
#     red = "\x1b[31;20m"
#     bold_red = "\x1b[31;1m"
#     reset = "\x1b[0m"
#     # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s " \
#     #          "(%(filename)s:%(lineno)d)"
#
#     _file_format = "(%(asctime)s) [%(levelname)s]: " \
#                    "%(name)s:%(filename)s:%(lineno)d %(message)s"
#
#
#     FORMATS = {
#         logging.DEBUG: grey + _file_format + reset,
#         logging.INFO: grey + _file_format + reset,
#         logging.WARNING: yellow + _file_format + reset,
#         logging.ERROR: red + _file_format + reset,
#         logging.CRITICAL: bold_red + _file_format + reset
#     }
#
#     def format(self, record):
#         log_fmt = self.FORMATS.get(record.levelno)
#         formatter = logging.Formatter(log_fmt)
#         return formatter.format(record)
