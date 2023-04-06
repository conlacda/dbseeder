from database import Database

db = Database(
    host="localhost",
    user="root",
    password="",
    database="seed"
)
# db.loadDatabase()
# print(db.tables)
db.makeSeed(rows_num = 1000000)