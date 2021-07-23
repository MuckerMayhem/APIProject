import os

import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import app.constants as constants
from app.database import SessionLocal

app = FastAPI(title=constants.API_TITLE,
              description=constants.API_DESCRIPTION,
              version=constants.API_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def root():
    msg = {"status": "running"}
    return msg
