from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.appointment import Patient
from schemas import CreatePatient,UpdatePatient


def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.patient_id == patient_id).first()


def get_patients(db: Session):
    return db.query(Patient).all()


def create_patient(db: Session, patient: CreatePatient):
    db_patient = Patient(**patient.model_dump())
    db.add(db_patient)
    
    db.commit()
    db.refresh(db_patient)
    return db_patient


def update_patient(db: Session, patient_id: int, patient_data: UpdatePatient):
    patient = db.query( Patient).filter( Patient.patient_id == patient_id).first()
    if not patient:
        return None

    patient.name = patient_data.name
    patient.info = patient_data.info
    patient.cellphone_number = patient_data.cellphone_number
   
    db.commit()
    db.refresh(patient)
    return patient


def delete_patient(db: Session, patient_id: int):
    patient = get_patient(db, patient_id)
    if patient:
        db.delete(patient)
        db.commit()
    return patient