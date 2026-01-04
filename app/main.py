from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# local modules
from . import models, schemas
from .database import engine, SessionLocal

# dbcreate
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# db connect
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# endpoint for teams
@app.get("/teams/", response_model=List[schemas.TeamRead])

def read_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    teams = db.query(models.Team).offset(skip).limit(limit).all()
    return teams
