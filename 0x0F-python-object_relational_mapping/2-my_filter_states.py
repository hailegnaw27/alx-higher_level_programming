#!/usr/bin/python3

"""
This script filters states by user input using MySQLdb.
"""

import sys
import MySQLdb

# Retrieve command-line arguments
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

# Establish a connection to the MySQL server
db = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Execute the SQL query
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
cursor.execute(query, (state_name,))

# Fetch the results and display them
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()
