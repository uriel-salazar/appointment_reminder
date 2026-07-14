from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os 

load_dotenv() 

DATABSE_URL = os.getenv("DATABASE_URL")
    
engine = create_engine(
    URL,echo=True)


class Base(DeclarativeBase):
    pass

