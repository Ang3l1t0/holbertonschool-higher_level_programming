#!/usr/bin/python3
"""Lists all states starting with passed arg, prevents injection"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
                user=argv[1],
                passwd=argv[2],
        db=argv[3])

    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM states\
        INNER JOIN cities ON states.id=cities.state_id ORDER BY id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
