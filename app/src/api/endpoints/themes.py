from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Theme])
def read_themes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve themes.
    """
    themes = crud.theme.get_multi(db, skip=skip, limit=limit)
    
    return themes


@router.post("/", response_model=schemas.Theme)
def create_theme(
    *,
    db: Session = Depends(deps.get_db),
    theme_in: schemas.ThemeCreate
) -> Any:
    """
    Create new theme.
    """
    theme = crud.theme.create(db=db, obj_in=theme_in)
    
    return theme


@router.put("/{id}", response_model=schemas.Theme)
def update_lieu(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    theme_in: schemas.ThemeUpdate
) -> Any:
    """
    Update un theme.
    """
    theme = crud.theme.get(db=db, id=id)
    theme = crud.theme.update(db=db, db_obj=theme, obj_in=theme_in)
    
    return theme


@router.get("/{id}", response_model=schemas.Theme)
def read_theme(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get theme by ID.
    """
    theme = crud.theme.get(db=db, id=id)
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")

    return theme


@router.delete("/{id}", response_model=schemas.Theme)
def delete_theme(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Supprimer un theme.
    """
    theme = crud.theme.get(db=db, id=id)
    if not theme:
        raise HTTPException(status_code=404, detail="Theme not found")

    theme = crud.theme.remove(db=db, id=id)
    return theme
