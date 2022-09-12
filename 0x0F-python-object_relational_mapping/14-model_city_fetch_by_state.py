#!/usr/bin/python3
"""
This is a generic text, will update
later
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


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

    my_query = session.query(
        State.name, City.name, City.id).join(State).order_by(City.id)

    print(my_query)

    for city in my_query:
        print(f"{city[0]}: ({city[2]}) {city[1]}")


if __name__ == '__main__':
    main()
