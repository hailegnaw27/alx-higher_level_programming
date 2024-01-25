#!/usr/bin/python3

"""
Prints the State object with the name passed as an argument from the hbtn_0e_6_usa database
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
    state_name = sys.argv[4]

    # Create the engine to connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')

    # Bind the engine to the Base class and create the session
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Query the State object with the name passed as an argument and print its id, or print "Not found" if no state matches the name
    state = session.query(State).filter(State.name == state_name).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
