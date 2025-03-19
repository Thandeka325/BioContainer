#!/usr/bin/env python3

"""
This script integrates with the FastAPI.
"""
from fastapi import FastAPI
from auth import auth_router

app = FastAPI()
app.include_router(auth_router)


@app.post("/api/containers")
def generate_container(config: dict):
    dockerfile = f"""
    FROM {config["os"]}
    RUN apt-get update && apt-get install -y {config["software"]}
    """
    return {"dockerfile": dockerfile}
