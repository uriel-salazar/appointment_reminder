from fastapi import APIRouter,Depends
from models.appointment import Appointment
from schemas import CreateAppointment
from sqlalchemy.orm import Session
from database.db import get_db
router = APIRouter()


@router.get("/{appointment_id}")
def get(appointment_id:int,db:Session = Depends(get_db)):
   return db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()

@router.post("")
def create_appointment(appointment:CreateAppointment,db:Session = Depends(get_db)):
    db_appointment= Appointment(**appointment.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment
