# xit2md

[![Run tests](https://github.com/chris48s/xit2md/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/chris48s/xit2md/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/chris48s/xit2md/branch/main/graph/badge.svg?token=8W93RI841H)](https://codecov.io/gh/chris48s/xit2md)
[![PyPI Version](https://img.shields.io/pypi/v/xit2md.svg)](https://pypi.org/project/xit2md/)
![License](https://img.shields.io/pypi/l/xit2md.svg)
![Python Compatibility](https://img.shields.io/badge/dynamic/json?query=info.requires_python&label=python&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fxit2md%2Fjson)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

[[x]it!](https://xit.jotaen.net/) is a plain-text file format for todos and check lists. xit2md converts a checklist in [x]it! format to markdown task lists. Markdown task lists are available in many markdown dialects including GitHub Flavored Markdown.

## Installation

```
pip install xit2md
```

## Usage

```python-repl
>>> from xit2md import xit2md_text

>>> xit = """Named Group
... [ ] Open
... [x] Checked
... [@] Ongoing
... [~] Obsolete
... """

>>> print(xit2md_text(xit, heading_level=2))
## Named Group
- [ ] Open
- [x] Checked
- [ ] Ongoing
- [x] ~Obsolete~
```
