from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import aiofiles
from src import crud, schemas
from src.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Lieu])
def read_lieux(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve lieux.
    """
    lieux = crud.lieu.get_multi(db, skip=skip, limit=limit)
    
    return lieux


@router.post("/", response_model=schemas.Lieu)
async def create_lieu(
    *,
    db: Session = Depends(deps.get_db),
    #lieu_in: schemas.LieuCreate, 
    in_file: UploadFile=File(...)
) -> Any:
    """
    Create new lieu.
    """
    async with aiofiles.open(out_file_path, 'wb') as out_file:
        content = await in_file.read()  # async read
        await out_file.write(content)  # async write

    return {"Result": "OK"}
    # lieu = crud.lieu.create(db=db, obj_in=lieu_in)
    # return lieu


@router.put("/{id}", response_model=schemas.Lieu)
def update_lieu(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    lieu_in: schemas.LieuUpdate
) -> Any:
    """
    Update un lieu.
    """
    lieu = crud.lieu.get(db=db, id=id)
    lieu = crud.lieu.update(db=db, db_obj=lieu, obj_in=lieu_in)
    
    return lieu


@router.get("/{id}", response_model=schemas.Lieu)
def read_lieu(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Get lieu by ID.
    """
    lieu = crud.lieu.get(db=db, id=id)
    if not lieu:
        raise HTTPException(status_code=404, detail="Lieu not found")

    return lieu


@router.delete("/{id}", response_model=schemas.Lieu)
def delete_lieu(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Delete an Lieu.
    """
    lieu = crud.lieu.get(db=db, id=id)
    if not lieu:
        raise HTTPException(status_code=404, detail="Lieu not found")

    lieu = crud.lieu.remove(db=db, id=id)
    return lieu


@router.get("/c/{id}", response_model=List[schemas.Lieu])
def read_lieux_by_categorie(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Retrieve lieux.
    """
    lieux = crud.lieu.get_multi_by(db, "categorie_id",id)
    
    return lieux


@router.get("/t/{id}", response_model=List[schemas.Lieu])
def read_lieux_by_theme(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> Any:
    """
    Retrieve lieux.
    """
    lieux = crud.lieu.get_multi_by(db, "theme_id",id)
    
    return lieux


@router.get("/s/{query}", response_model=List[schemas.Lieu])
def search_lieux(
    *,
    db: Session = Depends(deps.get_db),
    query: str
) -> Any:
    """
    rechercher lieux.
    """
    lieux = crud.lieu.search(query,db)
    
    return lieux