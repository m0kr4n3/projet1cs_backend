from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from src.crud.base import CRUDBase
from src.models.lieu import Lieu
from src.schemas.lieu import LieuCreate, LieuUpdate


class CRUDLieu(CRUDBase[Lieu, LieuCreate, LieuUpdate]):
    def create(
        self, db: Session, *, obj_in: LieuCreate
    ) -> Lieu:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List:
        result = (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )
        return result


lieu = CRUDLieu(Lieu)
