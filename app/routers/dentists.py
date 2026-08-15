from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from crud.dentist import create_dentist as crud_create_dentist
from app.crud.dentist import get_dentist as crud_get_dentist 
from app.crud.dentist import get_dentists as crud_get_dentists
from app.crud.dentist import update_dentist as crud_update_dentist
from app.crud.dentist import delete_dentist as crud_delete_dentist
from database.db import get_db
from schemas import CreateDentist,UpdateDentist

router = APIRouter()


@router.get("/{appointment_id}")
def get_dentist(dentist_id: int, db: Session = Depends(get_db)):
    if not dentist_id:
        raise HTTPException(status_code=404, detail="Dentist not found")

    return crud_get_dentist(db, dentist_id)
 
 # get all dentists 

@router.get("")
def get_dentists(db: Session = Depends(get_db)):
    """
    Get all dentists 
    """
    return crud_get_dentists(db)


@router.post("")
def create_dentist(dentist: CreateDentist, db: Session = Depends(get_db)):
    return crud_create_dentist(db, dentist)


@router.put("/{dentist_id}")
def update_existing_dentist(
    dentist_id: int,
    dentists: UpdateDentist,
    db: Session = Depends(get_db),
):
   if not dentist_id:
      raise HTTPException(status_code = 404,detail = "Dentist not found" )
  
   updated = crud_update_dentist(db, dentist_id, dentists)
   return updated



@router.delete("/{dentist_id}")
def delete_dentist(dentist_id: int, db: Session = Depends(get_db)):
    """
    -- Deletes dentist by id --

    """
    dentist = crud_delete_dentist(db, dentist_id)
    if not dentist:
        raise HTTPException(status_code=404, detail="Dentist not found")
    return {"detail": "Dentist deleted"}