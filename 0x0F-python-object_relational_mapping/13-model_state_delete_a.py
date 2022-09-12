#!/usr/bin/python3
"""
This is a generic text, will update
later
"""


import sys
from unicodedata import name
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, update)


def main():
    """
    This is a generic text, will update
    later
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
        )

    Base.metadata.create_all(engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    session.query(State).filter(
        State.name.ilike('%a%')).delete(synchronize_session='fetch')
    session.commit()


if __name__ == "__main__":
    main()
