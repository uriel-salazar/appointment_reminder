from datetime import date as date_type
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db import Base

if TYPE_CHECKING:
    from models.patient import Patient


class AppointmentStatus(str, Enum):
    SCHEDULED = "scheduled"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NO_SHOW = "no_show"


class Appointment(Base):
    __tablename__ = "appointment"

    appointment_id: Mapped[int] = mapped_column(primary_key=True)
    dentist_id: Mapped[int] = mapped_column(nullable=False)
    info: Mapped[str] = mapped_column(nullable=True)
    date: Mapped[date_type] = mapped_column(Date, nullable=False)
    status: Mapped[AppointmentStatus] = mapped_column(
        default=AppointmentStatus.SCHEDULED,
        nullable=False,
    )
    patient_id: Mapped[int] = mapped_column(ForeignKey("patient.patient_id"))

    patient: Mapped["Patient"] = relationship(back_populates = "appointments")
    
