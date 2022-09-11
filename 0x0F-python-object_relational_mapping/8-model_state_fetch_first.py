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

    main = session.query(State).order_by(State.id)
    states =  session.query(State).order_by(State.id).first()

    if main.count() == 0:
        print('Nothing')
    else:
        print(f"{states.id}: {states.name}")


if __name__ == '__main__':
    main()