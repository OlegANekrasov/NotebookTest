import uuid
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

import Models.type as model
import Schemas.typeSchema as typeSchema

def get_type(db: Session, type_id: str):
    return db.query(model.Type).filter(model.Type.id == type_id).first()

def get_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Type).offset(skip).limit(limit).all()

def get_type_by_name(db: Session, name: str):
    return db.query(model.Type).filter(model.Type.name == name).first()

def create_type(db: Session, name: str):
    typeCreate = model.Type(id = str(uuid.uuid4()), name=name)
    db.add(typeCreate)
    db.commit()
    db.refresh(typeCreate)
    return typeCreate

def update_type(db: Session, type: typeSchema.TypeUpdate):
    typeUpdate = db.query(model.Type).filter(model.Type.id == type.id).first()
    if typeUpdate == None:
        return JSONResponse(status_code=404, content={"message": "Type not found"})

    typeUpdate.name = type.name
    db.commit()
    db.refresh(typeUpdate)
    return typeUpdate
def delete_type(db: Session, type_id: str):
    typeDel = db.query(model.Type).filter(model.Type.id == type_id).first()
    if typeDel == None:
        return JSONResponse(status_code=404, content={"message": "Type not found"})

    db.delete(typeDel)
    db.commit()
    return typeDel