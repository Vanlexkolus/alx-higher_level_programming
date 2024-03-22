#!/usr/bin/python3
"""
This is a script thatg get State objects that have 'a'
from the database hbtn_0e_6_usa
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

    # Update record
    new_rec = session.query(State).filter(State.id == 2).first()
    new_rec.name = "New Mexico"
    session.commit()

    session.close()
