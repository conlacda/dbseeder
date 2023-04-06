from dataclasses import dataclass, field
from src.dbseeder.fields import Field


@dataclass
class Table:
    name: str = ""
    fields: list = field(default_factory=list)
    ignore_fields = ["id"]

    def addField(self, col):
        field = Field(col)
        if field.name not in self.ignore_fields:
            self.fields.append(Field(col))

    @property
    def field_names(self):
        return f"({','.join([f'`{field.name}`' for field in self.fields])})"

    @property
    def percent_s(self):
        # %s, %s
        result = ""
        for i in range(len(self.fields)):
            result += "%s,"
        result = result[:-1]
        return f"({result})"

    @property
    def fake_data(self):
        result = [field.fake_data for field in self.fields]
        return tuple(result)

    def genSQL(self, rows_num=10):
        # https://www.w3schools.com/python/python_mysql_insert.asp
        sql = f"INSERT INTO {self.name} {self.field_names} VALUES {self.percent_s}"
        val = [self.fake_data for i in range(rows_num)]
        return sql, val
