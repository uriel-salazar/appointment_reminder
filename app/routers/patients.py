from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.patient import Patient
from schemas import CreatePatient,UpdatePatient
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

@router.put("/patients/{patients_id}")
def update_patient(patient_id:int,patient_data:UpdatePatient,db:Session = Depends(get_db)):
    patient = db.get(Patient,patient_id)
    
    if patient is None:
        return None
    
    patient.info= patient_data.info
    patient.name = patient_data.name
    patient.cellphone_number = patient_data.cellphone_number
    
    
    


