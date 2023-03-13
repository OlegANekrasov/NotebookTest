from fastapi import FastAPI
from database import engine
from Controllers.TypeController import typeroute

import Models.type as ModelType, Models.object as ModelObject

ModelType.Base.metadata.create_all(bind=engine)
ModelObject.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(typeroute, prefix="/type")


