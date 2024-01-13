#!/usr/bin/python3
""" List all state objects using sqlalchemy """

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker, Session
    from model_state import Base, State
    from model_city import City

    nm = '{}'.format(argv[1])
    ps = '{}'.format(argv[2])
    dn = '{}'.format(argv[3])

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(nm, ps, dn))

    Session = sessionmaker(bind=engine)
    ses = Session()

    for state, city in ses.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

