import mysql.connector
from tqdm import tqdm

from dbseeder.table import Table


class Database:
    db = None
    tables = []
    batchSize = 100
    failed_query_num = 0

    def __init__(self, host="localhost", user="root", password="", database="") -> None:
        self.db = mysql.connector.connect(
            host=host, user=user, password=password, database=database
        )

    @property
    def table_names(self):
        cursor = self.db.cursor()
        cursor.execute("SHOW TABLES")
        return [x[0] for x in cursor]

    def column_names(self, table_name):
        cursor = self.db.cursor()
        cursor.execute("SHOW COLUMNS FROM " + table_name)
        return [x[0] for x in cursor]

    def loadDatabase(self):
        cursor = self.db.cursor()
        for table_name in self.table_names:
            table = Table(table_name)
            cursor.execute("SHOW COLUMNS FROM " + table_name)
            for col in cursor:
                table.addField(col)
            self.tables.append(table)

    def makeSeed(self, rows_num=10):
        self.loadDatabase()
        cursor = self.db.cursor()
        for table in self.tables:
            print(f"Make seed for table '{table.name}' - {rows_num} rows")
            for i in tqdm(range(rows_num // self.batchSize + 1)):
                sql, val = table.genSQL(
                    min(rows_num - i * self.batchSize, self.batchSize)
                )
                # Phần unique đoạn này không có sẽ gây ra lỗi
                try:
                    cursor.executemany(sql, val)
                    self.db.commit()
                except:
                    self.failed_query_num += 1
                    # print(sql, val)

        print(f"{self.failed_query_num} queries failed")

    def clearDatabase(self):
        for table in self.table_names:
            cursor = self.db.cursor()
            cursor.execute("DELETE FROM " + table)

    def clearAndMakeSeed(self, rows_num=10):
        self.clearDatabase()
        self.makeSeed(rows_num)
