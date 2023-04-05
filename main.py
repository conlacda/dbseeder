from database import Database

db = Database()
# db.loadDatabase()
# print(db.tables)
db.makeSeed(rows_num = 1000000)