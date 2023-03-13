from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Type(Base):
    __tablename__ = "types"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    #object = relationship('Object', back_populates='object')