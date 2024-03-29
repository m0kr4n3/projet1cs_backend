from sqlalchemy import Column, Integer, String
from src.db.base_class import Base


class Categorie(Base):
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True,unique=True)
    description = Column(String, index=True)
