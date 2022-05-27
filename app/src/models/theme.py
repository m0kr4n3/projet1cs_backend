from sqlalchemy import Column, Integer, String
from src.db.base_class import Base


class Theme(Base):
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    description = Column(String, index=True)