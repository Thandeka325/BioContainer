"""
This script handles User Authentication API with secure JWT tokens.
"""

import os
from dotenv import load_dotenv
import jwt
import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from backend.database import SessionLocal
from backend.models import User
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Load environment variables from .env file
load_dotenv()

# Secure Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")  # Use fallback for safety

# Password Hashing Context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

auth_router = APIRouter()

# Dependency: Get Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Generate JWT Token
def create_access_token(email: str):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    payload = {"email": email, "exp": expiration}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# Decode and Verify JWT Token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

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
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(user.email)
    return {"access_token": token}


# Get Current User from Token
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    email = payload.get("email")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    return email  # Return email or fetch user from DB if needed
