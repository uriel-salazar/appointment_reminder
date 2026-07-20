from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Patient
from schemas import CreatePatient
from database.db import get_db
router = APIRouter()

@router.get("/{patient_id}")
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    return db.query(Patient).filter(Patient.patient_id == patient_id).first()

@router.post("")
def create_patient(patient:CreatePatient ,db:Session = Depends(get_db)):
    db_patient = Patient(**patient.model_dump())
    
    db.add(patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

