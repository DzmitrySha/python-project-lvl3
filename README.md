# Page Loader

[![Actions Status](https://github.com/DzmitrySha/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/DzmitrySha/python-project-lvl3/actions)
[![workflow](https://github.com/DzmitrySha/python-project-lvl3/actions/workflows/pyci.yml/badge.svg)](https://github.com/DzmitrySha/python-project-lvl3/actions/workflows/pyci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/14654064fd831827f0c9/maintainability)](https://codeclimate.com/github/DzmitrySha/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/14654064fd831827f0c9/test_coverage)](https://codeclimate.com/github/DzmitrySha/python-project-lvl3/test_coverage)


---

## Instructions

**Install/uninstall package:**

`make package-install`
`make package-uninstall`

**Run help:**

`page-loader -h`

**Run script with default settings (save in current folder):** 

`page-loader <source_url>`

**Run script with user settings (save in exists output specified folder):** 

`page-loader --output <exist_folder_path> <source_url>`

or

`page-loader -o <exist_folder_path> <source_url> `

**If you get an error - see log file (page_loader.log):** 

`grep page_loader page_loader.log`

**You can use it as a python module:** 

`from page_loader import download`

`download(source_url, exist_folder_path)`

---

## Examples of using "Page Loader" (asciinems):

Download html page:

[![asciicast](https://asciinema.org/a/2xylreHjfyIbefJaaQrqz6dMO.svg)](https://asciinema.org/a/2xylreHjfyIbefJaaQrqz6dMO)

Download html page + resources:

[![asciicast](https://asciinema.org/a/zpoEkgTPWprl9v2Jwqgdxgsjh.svg)](https://asciinema.org/a/zpoEkgTPWprl9v2Jwqgdxgsjh)

Download html page + resources (with logging):

[![asciicast](https://asciinema.org/a/mWjoiaKEonFeBfFkTq3lZOIDU.svg)](https://asciinema.org/a/mWjoiaKEonFeBfFkTq3lZOIDU)

Logging errors:

[![asciicast](https://asciinema.org/a/I280X2RrvKKTkjDgWh5EwnmQy.svg)](https://asciinema.org/a/I280X2RrvKKTkjDgWh5EwnmQy)

Downloading with ChargingBars:

[![asciicast](https://asciinema.org/a/lwivpiIFkBcx40Igac1KHd1YQ.svg)](https://asciinema.org/a/lwivpiIFkBcx40Igac1KHd1YQ)