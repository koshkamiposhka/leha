from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class CustomUser(Base):
    __tablename__ = "users_customuser"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    telegram_id = Column(String, nullable=True)