#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from unicodedata import name
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, update)


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
    pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    states = session.query(State).filter(State.id == 2).first()
    if states:
        states.name = "New Mexico"
        session.add(states)
        session.commit()


if __name__ == '__main__':
    main()