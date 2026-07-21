from database.db import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import Date,ForeignKey
from enum import Enum

from .models import Patient
from datetime import date

class AppointmentStatus(str,Enum):
        SCHEDULED = "scheduled"
        CONFIRMED = "confirmed"
        COMPLETED = "completed"
        CANCELLED = "cancelled"
        NO_SHOW = "no_show"


class Appointment(Base):
    __tablename__ = 'appointment'
    appointment_id : Mapped[int] = mapped_column(primary_key= True)
    dentist_id: Mapped[int] = mapped_column(nullable = False)
    appointment_info: Mapped[str] = mapped_column(nullable = True)
    appointment_date : Mapped[date] = mapped_column(Date,nullable = False) 
    status: Mapped[AppointmentStatus] = mapped_column(
        default=AppointmentStatus.SCHEDULED,
        nullable=False
    )
    patient_id : Mapped[int] = mapped_column(
        ForeignKey('patient.patient_id')
    )
    
    patient : Mapped["Patient"] = relationship(
        back_populates = 'appointments'
    )