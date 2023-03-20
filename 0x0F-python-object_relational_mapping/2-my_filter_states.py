#!/usr/bin/python3
""" 
Lists all states from the database hbtn_0e_0_usa running on local host.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access database and print state that matches the argument given.
    """
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))
    r = cursor.fetchall()

    for row in r:
        print(row)
