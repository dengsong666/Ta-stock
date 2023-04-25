import sqlalchemy
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    enabled = Column(Boolean, default=True)
    selected = relationship("Item", back_populates="index")


class Selected(Base):
    __tablename__ = "stock_index"

    code = Column(String, primary_key=True)
    name = Column(String)
    source = Column(String)
    index_id = Column(Integer, ForeignKey("users.id"))

    index = relationship("User", back_populates="selected")
