import datetime

import sqlalchemy
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Command(Base):
    __tablename__ = 'command'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer, default=0)
    successes = Column(Integer, default=0)
    failures = Column(Integer, default=0)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "<Player(name='%s', score='%x', successes='%x', " \
            "failures='%s', created_date='%s')>" % (
                self.name,
                self.score,
                self.successes,
                self.failures,
                self.created_date
            )

engine = sqlalchemy.create_engine('sqlite:///../data.db', echo=True)
Base.metadata.create_all(engine)
