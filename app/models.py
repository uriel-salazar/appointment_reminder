from database.db import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import Date,ForeignKey
from enum import Enum
from datetime import date


class AppointmentStatus(str,Enum):
        SCHEDULED = "scheduled"
        CONFIRMED = "confirmed"
        COMPLETED = "completed"
        CANCELLED = "cancelled"
        NO_SHOW = "no_show "

class Patient(Base):
    __tablename__ = 'patient'
    patient_id:Mapped[int] = mapped_column(primary_key = True)
    patient_info: Mapped[str] = mapped_column(nullable = True)
    name : Mapped[str] = mapped_column(nullable = False)
    cellphone_number : Mapped[str] = mapped_column(unique = True, nullable = False)
    appointments: Mapped[list["Appointment"]] = relationship(
        back_populates='patient'
    )
    
    
class Appointment(Base):
    __tablename__ = 'appointment '
    appointment_id : Mapped[int] = mapped_column(primary_key= True)
    dentist_id: Mapped[int] = mapped_column(nullable = False)
    appointment_info: Mapped[str] = mapped_column(nullable = True)
    appointment_date : Mapped[date] = mapped_column(Date,nullable = False) 
    status: Mapped [AppointmentStatus] = mapped_column(
        AppointmentStatus.SCHEDULED,
        nullable = False
    )
    patient_id : Mapped[int] = mapped_column(
        ForeignKey('patient.id')
    )
    
    patient : Mapped["Patient"] = relationship(
        back_populates = 'appointment'
    )
