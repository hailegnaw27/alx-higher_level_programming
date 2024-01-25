#!/usr/bin/python3
"""
state creatoer
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sqlalchemy.engine.url import URL
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    usr = sys.argv[1]
    pas = sys.argv[2]
    dn = sys.argv[3]

    url = {'drivername': 'mysql+mysqldb', 'host': 'localhost',
           'username': usr, 'password': pas, 'database': dn}

    engine = create_engine(URL(**url), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    newState = State(name="California")
    newState.cities.append(City(name="San Francisco"))

    session.add(newState)
    session.commit()

