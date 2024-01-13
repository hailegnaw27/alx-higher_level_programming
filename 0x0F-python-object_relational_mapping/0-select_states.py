#!/usr/bin/python3
"""
list all stattrs
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # defalt port - 3306
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
