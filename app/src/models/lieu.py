from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float  
from src.db.base_class import Base


class Lieu(Base):
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    description = Column(String, index=True)
    longitude = Column(Float, index=True)
    latitude = Column(Float, index=True)
