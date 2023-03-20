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

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=hbtn_0e_0_usa)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY states.id")
    [print(state) for state in cur.fetchall()]

