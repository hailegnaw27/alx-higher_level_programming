#!/usr/bin/python3

"""
Filter states by user input
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Establish a connection to the MySQL server
    db = MySQLdb.connect(user=mysql_username, passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".format(state_name)
    cursor.execute(query)

    # Fetch the results and display them
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
