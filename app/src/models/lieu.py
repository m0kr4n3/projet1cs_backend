from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from src.db.base_class import Base


class Lieu(Base):
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True,unique=True)
    description = Column(String, index=True)
    longitude = Column(Float, index=True)
    latitude = Column(Float, index=True)
    categorie_id = Column(Integer, ForeignKey("categorie.id"))
    categorie = relationship("Categorie")
