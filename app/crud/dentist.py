from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.dentist import Dentist
from schemas import CreateDentist,UpdateDentist


def get_dentist(db: Session, dentist_id: int):
    return db.query(Dentist).filter(Dentist.dentist_id == dentist_id).first()


def get_dentists(db: Session):
    return db.query(Dentist).all()


def create_dentist(db: Session, dentist: CreateDentist):
    db_dentist = Dentist(**dentist.model_dump())
    db.add(db_dentist)
    
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Invalid dentist_id or doesn't exist.")
    db.refresh(db_dentist)
    return db_dentist


def update_dentist(db: Session, dentist_id: int, dentist_data: UpdateDentist):
    dentist = db.query(Dentist).filter(Dentist.dentist_id == dentist_id).first()
    if not dentist:
        return None
    dentist.name = dentist_data.name
    dentist.last_name = dentist_data.last_name
    dentist.phone = dentist_data.phone
    
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code = 409, detail = "Invalid dentist_id")
    db.refresh(dentist)
    return dentist


def delete_dentist(db: Session, dentist_id: int):
    dentist = get_dentist(db, dentist_id)
    if dentist:
        db.delete(dentist)
        db.commit()
    return dentist

