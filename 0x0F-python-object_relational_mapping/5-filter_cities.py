#!/usr/bin/python3

"""
List all cities of a given state from the hbtn_0e_4_usa database
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

    # Execute the SQL query using parameterized query with placeholders
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch the results and display them
    results = cursor.fetchall()
    cities = [row[0] for row in results]
    print(", ".join(cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()
