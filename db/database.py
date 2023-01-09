from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_PASSWORD = config('DB_PASSWORD')

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:"+DB_PASSWORD+"@localhost/pet-app"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
