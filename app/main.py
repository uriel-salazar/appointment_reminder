
from fastapi import FastAPI
from fastapi.responses import HTMLResponse,PlainTextResponse
import uvicorn
from sqlalchemy.orm import Session
from fastapi import HTTPException,Depends
from models import get_db,User
import crud
#from crud import create_user,get_users,update_user
from schemas import User_Create,User_Response
from database import Base,engine

app=FastAPI()
Base.metadata.create_all(bind=engine)

