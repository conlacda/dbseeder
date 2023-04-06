from faker import Faker
from dataclasses import dataclass
from datetime import datetime
import re

fake = Faker()
data_definitions = {
    "tinyint": {"min": -128, "max": 127, "type": "int"},
    "smallint": {"min": -(1 << 15), "max": 1 << 15 - 1, "type": "int"},
    "int": {"min": -(1 << 31), "max": 1 << 31 - 1, "type": "int"},
    "bigint": {"min": -(1 << 63), "max": 1 << 63 - 1, "type": "int"},
    "float": {"min": 0, "max": 3e38, "type": "int"},
    "double": {"min": 0, "max": 3e308, "type": "int"},
    "decimal": {"min": -128, "max": 0, "type": "int"},
    "varchar": {"min": 1, "max": 0, "type": "string"},
    "char": {"min": 1, "max": 0, "type": "string"},
    "text": {"min": 1, "max": 1 << 16 - 1, "type": "string"},
    "tinytext": {"min": 1, "max": 255, "type": "string"},
    "mediumtext": {"min": 1, "max": 1 << 24 - 1, "type": "string"},
    "longtext": {"min": 1, "max": 1 << 32 - 1, "type": "string"},
    "date": {"min": -1, "max": -1, "type": "timestamp"},
    "time": {"min": -1, "max": -1, "type": "timestamp"},
    "year": {"min": -1, "max": -1, "type": "timestamp"},
    "datetime": {"min": -1, "max": -1, "type": "timestamp"},
    "timestamp": {"min": -1, "max": -1, "type": "timestamp"},
}


@dataclass
class DataGen:
    type: str = ""
    size: int = 10

    def gen(self, data_type, min, max):
        type = data_definitions[data_type]["type"]
        # String - có giá trị ràng buộc độ dài min, max được định nghĩa sẵn
        if type == "string":
            return self.string(min, max)
        # Timestamp: không quan tâm min, max
        if type == "timestamp":
            return self.timeStamp()
        # Int - theo giá trị mặc định, không tính tới min, max
        if type == "int":
            return self.int(
                data_definitions[data_type]["min"], data_definitions[data_type]["max"]
            )

    def string(self, min_len, max_len):
        len = fake.random_int(min=min_len, max=max_len)
        text = fake.text()
        return text[:len]

    def timeStamp(self):
        return datetime.now()

    def int(self, min, max):
        return fake.random_int(min=min, max=max)


dataGen = DataGen()


@dataclass
class Field:
    name: str = ""
    data_type: str = ""
    nullable: bool = True
    default_value: str = ""
    key: str = ""  # PRI
    max: int = 0
    min: int = 0

    def __init__(self, data: tuple) -> None:
        self.name, type_size, self.nullable, self.key, self.default_value, __ = data
        self.getInfo(type_size)

    def getInfo(self, type_size):
        # text, longtext
        if "(" not in type_size:
            self.data_type = type_size
            return
        # bigint(20), int(12)
        reg = "(.*)\((\d{1,10})\)"
        matches = re.findall(reg, type_size)
        if len(matches) > 0:
            self.data_type = matches[0][0]
            self.max = int(matches[0][1])

    @property
    def fake_data(self):
        return dataGen.gen(self.data_type, self.min, self.max)
