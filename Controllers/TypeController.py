from fastapi import APIRouter, Depends, HTTPException
import Schemas.typeSchema as typeSchema
import Repository.TypeRepository as typeRepository

from sqlalchemy.orm import Session
from database import SessionLocal, engine

typeroute = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@typeroute.get("/GetAll", response_model=list[typeSchema.Type])
def read_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    types = typeRepository.get_types(db, skip=skip, limit=limit)
    return types

@typeroute.post("/Add/", response_model=typeSchema.Type)
def create_type(type: typeSchema.TypeCreate, db: Session = Depends(get_db)):
    typeCreate = typeRepository.get_type_by_name(db, name=type.name)
    if typeCreate:
        raise HTTPException(status_code=400, detail="Type already exists")
    return typeRepository.create_type(db=db, name=type.name)

@typeroute.put("/Update/", response_model=typeSchema.Type)
def update_type(type: typeSchema.TypeUpdate, db: Session = Depends(get_db)):
    #typeUpdate = typeRepository.get_type(db, type_id=type.id)
    return typeRepository.update_type(db=db, type=type )

@typeroute.delete("/Delete/", response_model=typeSchema.Type)
def delete_type(type: typeSchema.TypeDelete, db: Session = Depends(get_db)):
    type = typeRepository.get_type(db, type_id=type.id)
    return typeRepository.delete_type(db=db, type_id=type.id)