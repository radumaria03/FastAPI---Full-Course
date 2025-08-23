from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQL_DB_URL = 'sqlite:///./blog.db'

# create db engine first
engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})

# create the db session
SessionLocal= sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()