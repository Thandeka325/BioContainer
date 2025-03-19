#!/usr/bin/env python3

"""
This scripts a User Authentication API.
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import jwt, datetime
from database import SessionLocal
from models import User

SECRET_KEY = "your_secret_key"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

auth_router = APIRouter()

# Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)

# Create Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register New User
@auth_router.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    hashed_password = hash_password(password)
    new_user = User(username=username, email=email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

# User Login
@auth_router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not pwd_context.verify(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = jwt.encode({"email": user.email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, SECRET_KEY)
    return {"access_token": token}
