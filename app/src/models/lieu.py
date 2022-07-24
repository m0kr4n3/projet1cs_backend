from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from src.db.base_class import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .categorie import Categorie
    from .theme import Theme

class Lieu(Base):
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True,unique=True)
    description = Column(String, index=True)
    longitude = Column(Float, index=True)
    latitude = Column(Float, index=True)
    categorie = relationship("Categorie")
    categorie_id = Column(Integer, ForeignKey("categorie.id"))
    theme = relationship("Theme")
    theme_id = Column(Integer, ForeignKey("theme.id"))
    image_path = Column(String, index=True)
    