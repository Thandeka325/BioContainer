#!/usr/bin/env python3
"""
This script sets up the Database Connection
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://biocontainer_user:StrongPassword123!@localhost:5432/biocontainer_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
