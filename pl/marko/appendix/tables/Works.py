from sqlalchemy import Column, Integer, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .db_config import Base

class Work(Base):
    __tablename__ = 'works'

    id = Column(Integer, primary_key=True, autoincrement=True)
    building_id = Column(Integer, ForeignKey('buildings.id'), nullable=False)
    date = Column(Date, default=func.current_date())  # Miesiąc, w którym praca była wykonana
    description = Column(String, nullable=False)
    total_hours = Column(Numeric, nullable=False)  # Ilość roboczogodzin
    travel_cost = Column(Numeric, nullable=False)  # Koszt dojazdu
    vat_rate = Column(Numeric, nullable=False)  # Stawka VAT

    building = relationship("Building", back_populates="works")
    materials = relationship("Material", back_populates="work", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Work(id={self.id}, building_id={self.building_id}, date={self.date}, description={self.description})>"

Building.works = relationship("Work", order_by=Work.id, back_populates="building")
