from database.db import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship


class Dentist(Base):
    __tablename__ = 'dentist'
    dentist_id:Mapped[int] = mapped_column(primary_key = True)
    name:Mapped[str] = mapped_column(nullable = False)
    last_name:Mapped[str] = mapped_column(nullable = False)
    phone:Mapped[str] = mapped_column(nullable=False,unique=True)