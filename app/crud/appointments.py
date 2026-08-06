from models.appointment import Appointment
from sqlalchemy.orm import Session
from schemas import CreateAppointment


def create_appointment(db:Session,appointment:CreateAppointment):
    db_appointment = Appointment(**appointment.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointment(db:Session,appointment_id:int):
    return db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()
