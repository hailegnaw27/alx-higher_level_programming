#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the MySQL server
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    
    # Create a cursor object to interact with the database
    cursor = db.cursor()
    
    # Execute the SQL query to retrieve the states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the rows returned by the query
    rows = cursor.fetchall()
    
    # Print the results
    for row in rows:
        print(row)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()
