from sqlalchemy import  Column,  Integer, String,DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    confirm_password=Column(String)
    age=Column(Integer)
    department=Column(Integer)
    



class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    token = Column(String)  
