from pydantic import BaseModel
from app.models import AppointmentStatus

class CreatePatient(BaseModel):
    name:str
    patient_info:str
    cellphone_number:str
    
class CreateAppointment(BaseModel):
    appointment_info:str
    appointment_date:str
    status:AppointmentStatus
    


