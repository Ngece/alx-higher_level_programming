#!/usr/bin/python3
""" 
Lists all states from the database hbtn_0e_0_usa running on local host.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    access database and print the states
    """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.arg[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    r = cur.fetchall()

   for row in r:
       print(row)

