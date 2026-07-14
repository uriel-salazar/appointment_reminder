from database.db import Base
from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy import String
class Patients(Base):
    __tablename__='patients'
    patient_id:Mapped[int]= mapped_column(primary_key = True)
    name : Mapped[str]= mapped_column(nullable = False)
    