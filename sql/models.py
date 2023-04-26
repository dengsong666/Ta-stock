from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class SelectedIndex(Base):
    __tablename__ = "selected_index"
    id = Column(String, ForeignKey('users.id'), primary_key=True)
    code = Column(String, ForeignKey('indexs.code'), primary_key=True)
    index = relationship("Index", back_populates="users")
    user = relationship("User", back_populates="indexs")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    enabled = Column(Boolean, default=True)
    indexs = relationship("SelectedIndex", back_populates="user")

    class Config:
        orm_mode = True


class Index(Base):
    __tablename__ = 'indexs'
    code = Column(String, primary_key=True)
    name = Column(String)
    series = Column(String)
    classify = Column(String)
    size = Column(Integer)
    source = Column(String)
    users = relationship("SelectedIndex", back_populates="index")

    class Config:
        orm_mode = True
