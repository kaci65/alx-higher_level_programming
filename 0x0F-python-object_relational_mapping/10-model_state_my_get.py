#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
script should take 4 arguments: mysql username, mysql password, database
name and state name to search (SQL injection free)
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

    aux = 0
    state = session.query(State).filter(State.name == sys.argv[4])
    for row in state:
        print("{}".format(row.id))
        aux = 1
    if aux == 0:
        print("Not found")
    session.close()
