# Seeder for Mysql
[![Github action](https://github.com/conlacda/dbseeder/actions/workflows/action.yml/badge.svg)](https://github.com/conlacda/dbseeder/actions/workflows/action.yml)

> Load database then make seeds for it

## Install

```shell
$ pip install dbseeder
```

## Usage
```python
from dbseeder import Database
db = Database(host="localhost", user="root", password="", database="seed")
# Make seed without deleting the existence data
db.makeSeed(rows_num=100000)
# Delete data, then make seeds
db.clearAndMakeSeed(rows_num=100000)
```
OR
```shell
$ python -m dbseeder --host localhost --user root --password= --database seed --rows_num 100 --drop
```

## TODO
* Load relationship
* Add test
* Add comment to constraint data

## Test

```shell
python -m pytest
```

## Packing
* [Tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [Package on Pypi](https://pypi.org/project/dbseeder/)

## My note
To publish new version:
* Change version in `pyproject.toml`
* Build: `python -m build`
* Upload to testpypi: `py -m twine upload --repository testpypi dist/*`
* Upload to pypi: `py -m twine upload --repository pypi dist/*`
