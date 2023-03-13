from pydantic import BaseModel

class TypeBase(BaseModel):
    name: str

class TypeCreate(TypeBase):
    pass
class TypeUpdate(TypeBase):
    id: str
class TypeDelete(BaseModel):
    id: str

class Type(TypeBase):
    id: str

    class Config:
        orm_mode = True
