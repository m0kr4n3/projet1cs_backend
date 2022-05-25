from typing import Optional

from pydantic import BaseModel


# Shared properties
class CategorieBase(BaseModel):
    nom: Optional[str] = None
    description: Optional[str] = None

# Properties to receive on item creation
class CategorieCreate(CategorieBase):
    nom: str
    description: str


# Properties to receive on item update
class CategorieUpdate(CategorieBase):
    pass


# Properties shared by models stored in DB
class CategorieInDBBase(CategorieBase):
    id: int
    nom: str
    description: str
    class Config:
        orm_mode = True


# Properties to return to client
class Categorie(CategorieInDBBase):
    pass


# Properties properties stored in DB
class CategorieInDB(CategorieInDBBase):
    pass