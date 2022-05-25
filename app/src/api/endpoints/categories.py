from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Categorie])
def read_categories(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve categories.
    """
    categories = crud.categorie.get_multi(db, skip=skip, limit=limit)
    
    return categories


@router.post("/", response_model=schemas.Categorie)
def create_categorie(
    *,
    db: Session = Depends(deps.get_db),
    categorie_in: schemas.CategorieCreate
) -> Any:
    """
    Create new categorie.
    """
    categorie = crud.categorie.create(db=db, obj_in=categorie_in)
    
    return categorie


@router.put("/{id}", response_model=schemas.Categorie)
def update_lieu(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    categorie_in: schemas.CategorieUpdate
) -> Any:
    """
    Update une categorie.
    """
    categorie = crud.categorie.get(db=db, id=id)
    categorie = crud.categorie.update(db=db, db_obj=categorie, obj_in=categorie_in)
    
    return categorie


@router.get("/{id}", response_model=schemas.Categorie)
def read_categorie(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get categorie by ID.
    """
    categorie = crud.categorie.get(db=db, id=id)
    if not categorie:
        raise HTTPException(status_code=404, detail="Categorie not found")

    return categorie


@router.delete("/{id}", response_model=schemas.Categorie)
def delete_categorie(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Delete une categorie.
    """
    categorie = crud.categorie.get(db=db, id=id)
    if not categorie:
        raise HTTPException(status_code=404, detail="Categorie not found")

    categorie = crud.categorie.remove(db=db, id=id)
    return categorie
