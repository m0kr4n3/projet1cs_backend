from typing import Optional, Tuple

from pydantic import BaseModel


# Shared properties
class RatingBase(BaseModel):
    user_id: Optional[int] = None
    lieu_id: Optional[int] = None
    stars: Optional[int] = None
# Properties to receive on item creation
class RatingCreate(RatingBase):
    user_id: int
    lieu_id: int
    stars: int


# Properties to receive on item update
class RatingUpdate(RatingBase):
    pass


# Properties shared by models stored in DB
class RatingInDBBase(RatingBase):
    user_id: int
    lieu_id: int
    stars: int
    # geo: List[float]
    class Config:
        orm_mode = True


# Properties to return to client
class Rating(RatingInDBBase):
    pass


# Properties properties stored in DB
class RatingInDB(RatingInDBBase):
    pass