from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.patient import Patient
from schemas import CreatePatient,UpdatePatient

from crud.patients import create_patient as crud_create_patient
from crud.patients import delete_patient as crud_delete_patient
from database.db import get_db
router = APIRouter()

@router.get("/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    return db.query(Patient).filter(Patient.patient_id == patient_id).first()

@router.post("")
def create_patient(patient:CreatePatient ,db:Session = Depends(get_db)):
    db_patient = Patient(**patient.model_dump())
    
    db.add(db_patient)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Patient with this cellphone number already exists")
    db.refresh(db_patient)
    return db_patient

@router.put("/{patient_id}")
def update_patient(patient_id:int,patient_data:UpdatePatient,db:Session = Depends(get_db)):
    patient = db.get(Patient,patient_id)
    
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    patient.info= patient_data.info
    patient.name = patient_data.name
    patient.cellphone_number = patient_data.cellphone_number
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code = 409, detail="Patient with this cellphone number already exists")
    db.refresh(patient)
    return patient
    
    
@router.delete("/{patient_id}")
def delete_patient(patient_id:int, db: Session = Depends(get_db)):
    patient = crud_delete_patient(db,patient_id)
    if not patient:
        raise HTTPException(status_code = 404,detail =" Patient not found ")


