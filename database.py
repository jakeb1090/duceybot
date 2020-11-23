from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#engine, base, session_
engine = create_engine('sqlite:///ducey.db')    #db

Base = declarative_base()                       #db.model
Base.metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)             #db.session
session = Session()
