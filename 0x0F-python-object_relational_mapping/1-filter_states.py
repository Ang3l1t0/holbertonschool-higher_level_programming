#!/usr/bin/python3
"""Lists all states with a name starting with N"""

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
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith('N'):
            print(row)
    cur.close()
    conn.close()
