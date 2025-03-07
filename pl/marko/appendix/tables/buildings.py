from sqlalchemy import Column, Integer, String
from pl.marko.appendix.db_config import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Building(Base):
    __tablename__ = 'buildings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String, unique=False, nullable=False)  # Budynki mogą się powtarzać w różnych miesiącach

    def __repr__(self):
        return f"<Building(id={self.id}, address={self.address})>"