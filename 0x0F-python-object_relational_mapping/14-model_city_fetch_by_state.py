#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usa"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from model_state import Base, State
from model_city import City
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

    aux = session.query(State, City).join(City).order_by(City.id).all():
        for i in aux:
            print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
    session.close()
