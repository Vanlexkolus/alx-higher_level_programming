#!/usr/bin/python3
"""
Write a script that lists all State objects from the
database hbtn_0e_6_usa

Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running
on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example
below
Your code should not be executed when imported
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
