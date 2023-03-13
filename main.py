from fastapi import Depends, FastAPI, Body, HTTPException
from fastapi.responses import JSONResponse, FileResponse

from database import SessionLocal, engine
from sqlalchemy.orm import Session
from Controllers.TypeController import typeroute

import Models.type as ModelType, Models.object as ModelObject
import Schemas.typeSchema as typeSchema
import Repository.TypeRepository as typeRepository

ModelType.Base.metadata.create_all(bind=engine)
ModelObject.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(typeroute, prefix="/type")

# Dependency
#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

#@app.get("/")
#def main():
#    return FileResponse("public/index.html")

#@app.get("/types", response_model=list[typeSchema.Type])
#def read_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#    types = typeRepository.get_types(db, skip=skip, limit=limit)
#    return types

#@app.post("/types")
#def create_type(data  = Body(), db: Session = Depends(get_db)):
#    type = ModelType.Type(id = 10, name='name1')
#    db.add(type)
#    db.commit()
#    db.refresh(type)
#    return type

