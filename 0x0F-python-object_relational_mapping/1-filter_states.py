#!/usr/bin/python3
"""script that lists all states with a name starting with N"""
import MySQLdb
import sys


def print_states_with_N(argv):
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE 'N%'
                   ORDER BY id""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    print_states_with_N(sys.argv)
