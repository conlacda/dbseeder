# Seeder for Mysql
[![gh-action-pip-audit](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml/badge.svg)](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml)

> Load database then make seeds for it

## Usage
```python
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
https://packaging.python.org/en/latest/tutorials/packaging-projects/