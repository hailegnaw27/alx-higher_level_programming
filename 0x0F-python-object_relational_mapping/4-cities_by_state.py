#!/usr/bin/python3

"""
List all cities from the hbtn_0e_4_usa database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Establish a connection to the MySQL server
    db = MySQLdb.connect(user=mysql_username, passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)

    # Fetch the results and display them
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
