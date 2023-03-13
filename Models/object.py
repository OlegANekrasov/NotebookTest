from sqlalchemy import  Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Object(Base):
    __tablename__ = "objects"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    typeId = Column(String, ForeignKey('types.id'))
    #type = relationship('Type', back_populates='type')