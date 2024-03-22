#!/usr/bin/python3
"""
This is a script thatg get first State objects from the database hbtn_0e_6_usa
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

    # Get first state object from database
    first_state = session.query(State).order_by(State.id).first()

    if not first_state:
        print("Nothing")
    else:
        print("{:d}: {:s}".format(first_state.id, first_state.name))

    session.close()
