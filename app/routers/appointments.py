from fastapi import APIRouter,Depends
from models.appointment import Appointment
from schemas import CreateAppointment,UpdateAppointment
import crud
from sqlalchemy.orm import Session
from database.db import get_db
router = APIRouter()


@router.get("/{appointment_id}")
def get(appointment_id:int,db:Session = Depends(get_db)):
   return db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()

@router.post("")
def create_appointment(appointment:CreateAppointment,db:Session = Depends(get_db)):
    db_appointment = Appointment(**appointment.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment
 
@router.put("/{appointment_id}")
def update_appointment(appointment_id:int,db:Session = Depends(get_db)):
   return db.query(Appointment).filter(Appointment.appointment_id == appointment_id).first()

@router.delete("/{appointment_id}")
def delete_appointment(appointment_id:int,db:Session = Depends(get_db)):
   return