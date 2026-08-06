from datetime import date as date_type

from pydantic import BaseModel

from models.appointment import AppointmentStatus

class PatientBase(BaseModel):
    name:str
    info:str
    cellphone_number:str


class CreatePatient(PatientBase):
    pass
    
class UpdatePatient(PatientBase):
    pass


class AppointmentBase(BaseModel):
    info:str
    date:date_type
    status:AppointmentStatus
    
class CreateAppointment(AppointmentBase):
    pass


class UpdateAppointment(AppointmentBase):
    pass



    


