from fastapi import APIRouter
from sqlalchemy.orm import Session
router = APIRouter()

@router.get("")
def get_patient():
    pass


