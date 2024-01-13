#!/usr/bin/python3

"""
Adds the State object "Louisiana" to the hbtn_0e_6_usa database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')

    # Bind the engine to the Base class and create the session
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Create a new State object with the name "Louisiana" and add it to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the newly created state
    print(new_state.id)

    # Close the session
    session.close()
