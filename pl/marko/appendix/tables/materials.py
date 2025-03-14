from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from pl.marko.appendix.db_config import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True, autoincrement=True)
    work_id = Column(Integer, ForeignKey('works.id'), nullable=False)
    name = Column(String, nullable=False)
    quantity = Column(Numeric, nullable=False)

    work = relationship("Work", back_populates="materials")

    def __repr__(self):
        return f"<Material(id={self.id}, name={self.name}, quantity={self.quantity})>"
