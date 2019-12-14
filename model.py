from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker


ENGINE = create_engine('sqlite:///db.sqlite3', echo=True)
Base = declarative_base()

session = scoped_session(
    sessionmaker(
        bind=ENGINE,
        autocommit=False,
    )
)


class Conversation(Base):
    __tablename__ = 'conversation'
    id = Column('id', Integer, primary_key=True)
    text = Column('name', Text)
    speaked_at = Column('speaked_at', DateTime)


Base.metadata.create_all(ENGINE)
