#!/usr/bin/python3
"""
This is a script that lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get all state object from database
    state = session.query(State).order_by(State.id)

    for objects in state:
        print("{:d}: {:s}".format(objects.id, objects.name))

    session.close()
