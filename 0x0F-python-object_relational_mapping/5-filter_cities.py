#!/usr/bin/python3
""" script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys


def print_states(argv):
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()

    cursor.execute("""SELECT c.name
            FROM cities as c INNER JOIN states as s ON s.id = c.state_id
            WHERE BINARY s.name = %s
            ORDER BY c.id ASC""", (argv[4], ))
    rows = cursor.fetchall()
    print(', '.join(item[0] for item in rows))
    cursor.close()
    db.close()


if __name__ == "__main__":
    print_states(sys.argv)
