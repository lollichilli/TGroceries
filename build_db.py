"""Building the DB"""

import csv
import os
from config import db
from models import Products


def build_db(filename):
    if os.path.exists(f"{filename}.sqlite3"):
        os.remove(f"{filename}.sqlite3")

    db.create_all()

    with open("for-population.csv") as f:
        content = csv.reader(f)
        next(content)

        for line in content:
            title = Products(
                name = line[0],
                kind = line[1],
                owner = line[2],
                price = line[3]
            )
            db.session.add(title)
        db.session.commit()


def main():
    build_db("products")

if __name__ == "__main__":
    main()

