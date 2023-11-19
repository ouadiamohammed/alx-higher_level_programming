#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def print_states(argv):
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()

    cursor.execute("""SELECT c.id, c.name, s.name
            FROM cities as c INNER JOIN states as s ON s.id = c.state_id
            ORDER BY c.id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    print_states(sys.argv)
