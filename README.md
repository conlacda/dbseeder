# Seeder for Mysql
[![gh-action-pip-audit](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml/badge.svg)](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml)

> Load database then make seeds for it

## Usage
```python
from dbseeder import Database
db = Database(host="localhost", user="root", password="", database="seed")
# Make seed without deleting the existence data
db.makeSeed(rows_num=100000)
# Delete data, then make seeds
db.clearAndMakeSeed(rows_num=100000)
```

## TODO
* Load relationship
* Add test
* Add argparser

## Test

```shell
python -m pytest
```

## Packing
* [Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [Pypi package](https://pypi.org/project/dbseeder/)

## My note
To publish new version:
* Change version in `pyproject.toml`
* Build: `python -m build`
* Upload to testpypi: `py -m twine upload --repository testpypi dist/*`
* Upload to pypi: `py -m twine upload --repository pypi dist/`