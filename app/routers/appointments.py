from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from models.appointment import Appointment
from schemas import CreateAppointment,UpdateAppointment
from crud.appointments import update_appointment,create_appointment,get_appointment
from sqlalchemy.orm import Session
from database.db import get_db
router = APIRouter()


@router.get("/{appointment_id}")
def get(db:Session = Depends(get_db),appointment_id:int):
   if not appointment_id:
      raise HTTPException(status_code = 404, detail ='Appointment not found')
   
   return get_appointment(db,appointment_id)

@router.post("")
def create_appointment(db:Session = Depends(get_db),appointment:CreateAppointment):
    return create_appointment(db,appointment)
 
@router.put("/{appointment_id}")
def update_existing_appointment(db:Session = Depends(get_db),appointment_id:int,appointment:UpdateAppointment):
   update_appointment = appointments.update_appointment(
      db,
      appointment_id=,
      appointment)
   return appointments.update_appointment(db,appointment_id)

@router.delete("/{appointment_id}")
def delete_appointment(appointment_id:int,db:Session = Depends(get_db)):
   if not appointment_id:
      raise HTTPException(status_code=404,detail='Appointment not found')
   
   return 