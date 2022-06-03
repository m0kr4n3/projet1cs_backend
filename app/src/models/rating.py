from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, CheckConstraint
from src.db.base_class import Base
from typing import TYPE_CHECKING
import enum 

if TYPE_CHECKING:
    from .user import User
    from .lieu import Lieu

# class Stars(enum.Enum):
#     zero = 0
#     one = 1
#     two = 2
#     three = 3
#     four = 4
#     five = 5

class Rating(Base):
    user = relationship("User")
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    lieu = relationship("Lieu")
    lieu_id = Column(Integer, ForeignKey("lieu.id"), primary_key=True)
    stars = Column(Integer,index=True, nullable=False)
    description = Column(String, nullable=True)
    CheckConstraint('stars >= 0 & stars <=5', name="stars_0_5")
    

    