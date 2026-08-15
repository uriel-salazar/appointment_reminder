from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.dentist import Dentist
from schemas import creat, UpdateAppointment


def get_appointment(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()


def get_appointments(db: Session):
    return db.query(Appointment).all()


def create_appointment(db: Session, appointment: CreateAppointment):
    db_appointment = Appointment(**appointment.model_dump())
    db.add(db_appointment)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Invalid patient_id or dentist_id")
    db.refresh(db_appointment)
    return db_appointment


def update_appointment(db: Session, appointment_id: int, appointment_data: UpdateAppointment):
    appointment = db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()
    if not appointment:
        return None

    appointment.info = appointment_data.info
    appointment.date = appointment_data.date
    appointment.status = appointment_data.status
    appointment.dentist_id = appointment_data.dentist_id
    appointment.patient_id = appointment_data.patient_id

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Invalid patient_id or dentist_id")
    db.refresh(appointment)
    return appointment


def delete_appointment(db: Session, appointment_id: int):
    appointment = get_appointment(db, appointment_id)
    if appointment:
        db.delete(appointment)
        db.commit()
    return appointment

