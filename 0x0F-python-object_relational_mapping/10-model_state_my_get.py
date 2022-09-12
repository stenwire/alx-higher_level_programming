#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
    pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    state_arg = sys.argv[4]
    states =  session.query(State).filter(State.name == state_arg).order_by(State.id)

    if states.first():
        for state in states:
            print(f"{state.id}")
    else:
        print("Not found")


if __name__ == '__main__':
    main()