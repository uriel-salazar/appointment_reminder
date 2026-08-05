from database.db import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship
from models.appointment import Appointment

class Patient(Base):
    __tablename__ = 'patient'
    patient_id:Mapped[int] = mapped_column(primary_key = True)
    info: Mapped[str] = mapped_column(nullable = True)
    name : Mapped[str] = mapped_column(nullable = False)
    cellphone_number : Mapped[str] = mapped_column(unique = True, nullable = False)
    appointments: Mapped[list["Appointment"]] = relationship(
        back_populates='patient'
    )