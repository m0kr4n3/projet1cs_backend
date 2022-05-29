from typing import Optional, Tuple

from pydantic import BaseModel


# Shared properties
class LieuBase(BaseModel):
    nom: Optional[str] = None
    description: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    categorie_id: Optional[int] = None
# Properties to receive on item creation
class LieuCreate(LieuBase):
    nom: str
    description: str


# Properties to receive on item update
class LieuUpdate(LieuBase):
    pass


# Properties shared by models stored in DB
class LieuInDBBase(LieuBase):
    id: int
    nom: str
    description: str = None
    # geo: List[float]
    class Config:
        orm_mode = True


# Properties to return to client
class Lieu(LieuInDBBase):
    pass


# Properties properties stored in DB
class LieuInDB(LieuInDBBase):
    pass