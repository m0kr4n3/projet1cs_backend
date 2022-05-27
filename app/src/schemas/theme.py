from typing import Optional

from pydantic import BaseModel


# Shared properties
class ThemeBase(BaseModel):
    nom: Optional[str] = None
    description: Optional[str] = None

# Properties to receive on item creation
class ThemeCreate(ThemeBase):
    nom: str
    description: str


# Properties to receive on item update
class ThemeUpdate(ThemeBase):
    pass


# Properties shared by models stored in DB
class ThemeInDBBase(ThemeBase):
    id: int
    nom: str
    description: str
    class Config:
        orm_mode = True


# Properties to return to client
class Theme(ThemeInDBBase):
    pass


# Properties properties stored in DB
class ThemeInDB(ThemeInDBBase):
    pass