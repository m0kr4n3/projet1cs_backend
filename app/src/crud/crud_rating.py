from typing import Any, Dict, List, Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import or_
from src.crud.base import CRUDBase
from src.models.rating import Rating
from src.schemas.rating import RatingCreate, RatingUpdate
from sqlalchemy.exc import IntegrityError

class CRUDRating(CRUDBase[Rating, RatingCreate, RatingUpdate]):
    def get(self, db: Session, user_id: int, lieu_id: int) -> Rating:
        return db.query(self.model).filter(self.model.user_id == user_id,self.model.lieu_id == lieu_id).first()

    def update(
        self,
        db: Session,
        *,
        db_obj: Any,
        obj_in: Union[RatingUpdate, Dict[str, Any]]
    ) -> Rating:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.__dict__
        print(obj_data,update_data)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj 

    def create(
        self, db: Session, *, obj_in: RatingCreate
    ) -> Rating:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        
        try:
            db.add(db_obj)
            db.commit()
            db.refresh(db_obj)
        except IntegrityError :
            db.rollback()
            # obj = db.query(self.model).filter(self.model.user_id == obj_in_data.get('user_id'),self.model.lieu_id == obj_in_data.get('lieu_id')).first()
            # db.delete(obj)
            # db.commit()
            self.remove(db,user_id=obj_in_data.get('user_id'),lieu_id=obj_in_data.get('lieu_id'))
            db.rollback()
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
    def remove(self, db: Session, *, user_id: int, lieu_id: int) -> Rating:
        obj = db.query(self.model).filter(self.model.user_id == user_id,self.model.lieu_id == lieu_id).first()
        db.delete(obj)
        db.commit()
        return obj





rating = CRUDRating(Rating)
