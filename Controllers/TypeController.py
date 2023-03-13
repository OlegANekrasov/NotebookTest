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

@typeroute.get("/types", response_model=list[typeSchema.Type])
def read_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    types = typeRepository.get_types(db, skip=skip, limit=limit)
    return types

@typeroute.post("/types/", response_model=typeSchema.Type)
def create_type(type: typeSchema.TypeCreate, db: Session = Depends(get_db)):
    db_user = typeRepository.get_type_by_name(db, name=type.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Type already exists")
    return typeRepository.create_type(db=db, type=type)