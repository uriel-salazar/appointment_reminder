from models.appointment import Appointment
from sqlalchemy.orm import Session
from schemas import CreateAppointment,UpdateAppointment


def get_appointment(db:Session,appointment_id:int):
    return db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()

def get_appointments(db:Session):
    return db.query(Appointment).all()


def create_appointment(db:Session,appointment:CreateAppointment):
    db_appointment = Appointment(**appointment.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def update_appointment(db:Session,appointment_id:int,appointment_data:UpdateAppointment):
    appointment = db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()
    if not appointment:
        return None
    
    appointment.info=  appointment_data.info
    appointment.date = appointment_data.date
    appointment.status = appointment_data.status
    
    
    db.commit()
    db.refresh(appointment)
    return appointment


def delete_appointment(db:Session,appointment_id:int):
    appointment = get_appointment(db,appointment_id)
    if appointment:
        db.delete(appointment)
        db.commit()
    return appointment



