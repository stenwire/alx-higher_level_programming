#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from unicodedata import name
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, update)

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
    .format(sys.argv[1], sys.argv[2], sys.argv[3]),
pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

new_state = State(name='Louisiana')
session.add(new_state)
session.commit()
states = session.query(State).filter(State.name == 'Louisiana')\
    .one_or_none()

# cur.execute("select * from states where name like binary 'N%';")
obj = "%{}%".format('a')
my_query = session.query(State).filter(State.name.like(obj)).all()
session.delete(my_query)
session.commit()

print(f"{states.id}")