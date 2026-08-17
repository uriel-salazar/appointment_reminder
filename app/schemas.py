from datetime import date as date_type
from pydantic import BaseModel
from models.appointment import AppointmentStatus


# Patient Schemas : 
class PatientBase(BaseModel):
    name:str
    info:str
    cellphone_number:str


class CreatePatient(PatientBase):
    pass
    
class UpdatePatient(PatientBase):
    pass

# Appointment Schemas : 
class AppointmentBase(BaseModel):
    info:str
    date:date_type
    status:AppointmentStatus
    dentist_id:int
    patient_id:int
    
class CreateAppointment(AppointmentBase):
    pass


class UpdateAppointment(AppointmentBase):
    pass

#  Dentist's Schemas  :
class DentistBase(BaseModel):
    name: str
    last_name: str 
    phone:str
    
    
class CreateDentist(DentistBase):
    pass
    
    
class UpdateDentist(DentistBase):
    pass




    
