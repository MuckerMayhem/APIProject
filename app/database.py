import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()

user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
hostname = os.environ.get("DB_HOST")
db = os.environ.get("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{hostname}/{db}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
