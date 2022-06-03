from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Rating])
def read_lieux(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve ratings.
    """
    ratings = crud.rating.get_multi(db, skip=skip, limit=limit)
    
    return ratings


@router.post("/", response_model=schemas.Rating)
def create_rating(
    *,
    db: Session = Depends(deps.get_db),
    rating_in: schemas.RatingCreate
) -> Any:
    """
    Create new rating.
    """
    rating = crud.rating.create(db=db, obj_in=rating_in)
    return rating





@router.get("/{id}", response_model=schemas.Rating)
def read_rating(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get rating by ID.
    """
    rating = crud.rating.get(db=db, id=id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")

    return rating


@router.delete("/{user_id}/{lieu_id}", response_model=schemas.Rating)
def delete_rating(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    lieu_id: int

) -> Any:
    """
    Delete an Rating.
    """
    rating = crud.rating.get(db=db, user_id=user_id, lieu_id=lieu_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")

    rating = crud.rating.remove(db=db, user_id=user_id, lieu_id=lieu_id)
    return rating

@router.get("/{id}", response_model=schemas.Rating)
def read_rating(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get rating by ID.
    """
    rating = crud.rating.get(db=db, id=id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")

    return rating