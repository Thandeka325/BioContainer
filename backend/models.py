"""
This script defines the Database Models
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Container(Base):
    __tablename__ = "containers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    software = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(String)

    user = relationship("User", back_populates="containers")
