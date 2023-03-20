#!/usr/bin/python3
""" 
Lists all states from the database hbtn_0e_0_usa running on local host.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access database and print all cities based on state name which 
    provided as an argument.
    """
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT *cities.id, cities.name FROM cities JOIN states ON states.id = cities.state_id WHERE states.name LIKE BINARY %(state_name)s ORDER BY cities.id ASC")
    r = cursor.fetchall()

    for row in r:
        print(row)
