# from src.dbseeder import Database
from src.dbseeder.database import Database

db = Database(host="localhost", user="root", password="", database="seed")
# db.makeSeed(rows_num=100)
db.clearAndMakeSeed(rows_num=100)
