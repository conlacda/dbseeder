from src.dbseeder import Database


def test_run():
    db = Database(host="localhost", user="root", password="", database="seed")
    db.makeSeed(rows_num=100)
