from pydantic import BaseModel


class CreatePatient(BaseModel):
    patient_info:str
    name:str
    cellphone_number:str
    


