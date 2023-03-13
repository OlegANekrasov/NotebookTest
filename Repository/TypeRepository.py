import uuid
from sqlalchemy.orm import Session

import Models.type as model
import Schemas.typeSchema as typeSchema

def get_type(db: Session, type_id: int):
    return db.query(model.Type).filter(model.Type.id == type_id).first()

def get_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Type).offset(skip).limit(limit).all()

def get_type_by_name(db: Session, name: str):
    return db.query(model.Type).filter(model.Type.name == name).first()

def create_type(db: Session, type: typeSchema.TypeCreate):
    db_type = model.Type(id = str(uuid.uuid4()), name=type.name)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

