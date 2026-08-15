from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from crud.appointments import create_appointment as crud_create_appointment
from crud.appointments import get_appointment as crud_get_appointment
from crud.appointments import get_appointments as crud_get_appointments
from crud.appointments import update_appointment as crud_update_appointment
from crud.appointments import delete_appointment as crud_delete_appointment
from database.db import get_db
from schemas import CreateAppointment, UpdateAppointment

router = APIRouter()


@router.get("/{appointment_id}")
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    if not appointment_id:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return crud_get_appointment(db, appointment_id)
 
 
@router.get("")
def get_appointments(db: Session = Depends(get_db)):
    return crud_get_appointments(db)


@router.post("")
def create_appointment(appointment: CreateAppointment, db: Session = Depends(get_db)):
    return crud_create_appointment(db, appointment)


@router.put("/{appointment_id}")
def update_existing_appointment(
    appointment_id: int,
    appointment: UpdateAppointment,
    db: Session = Depends(get_db),
):
   if not appointment_id:
      raise HTTPException(status_code = 404,detail = "Appointment not found" )
   updated = crud_update_appointment(db, appointment_id, appointment)
   if updated is None:
      raise HTTPException(status_code=404, detail="Appointment not found")
   return updated


@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = crud_delete_appointment(db, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
<<<<<<< HEAD
    return {"detail": "Appointment deleted"}
=======
    return {"detail": "Appointment deleted"}
>>>>>>> dev
