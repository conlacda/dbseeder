from database import Database

db = Database(host="localhost", user="root", password="", database="seed")
db.makeSeed(rows_num=20)
