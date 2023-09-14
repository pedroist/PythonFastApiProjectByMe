from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234!@localhost/TodoApplicationDatabase"
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:<D****022$>@127.0.0.1:3306/TodoApplicationDatabase"
# mysql takes the password defined for mysql on the mysql workbench

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
