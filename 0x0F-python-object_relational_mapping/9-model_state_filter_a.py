#!/usr/bin/python3
"""
script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from model_state import Base, State
import sys


if __name__ == "__main__":
    db_url = {'user': 'sys.argv[1]',
              'passwd': 'sys.argv[2]',
              'db': 'sys.argv[3]',
              'host': 'localhost',
              'port': 3306}

    engine = create_engine(URL(**db_url))
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.in_(['a']))
    for row in state:
        print("{}: {}".format(row.id, row.name))
    session.close()
