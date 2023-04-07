from dbseeder import database
import argparse

parser = argparse.ArgumentParser(description="Make seeds for MySQL")

parser.add_argument(
    "--host", default="localhost", help="host - default: localhost", type=str
)
parser.add_argument("--user", default="root", help="user - default: root", type=str)
parser.add_argument("--password", help="database's password", type=str, default="")
parser.add_argument("--database", required=True, help="database", type=str)
parser.add_argument(
    "--rows_num",
    help="The number of row needs to be added - default: 100",
    type=int,
    default=100,
)
parser.add_argument(
    "--drop", action="store_true", default=False, help="drop table before making seeds"
)
args = parser.parse_args()


def main():
    db = database.Database(
        host=args.host, user=args.user, password=args.password, database=args.database
    )
    if args.drop:
        db.clearAndMakeSeed(rows_num=args.rows_num)
    else:
        db.makeSeed(rows_num=100)


if __name__ == "__main__":
    main()
