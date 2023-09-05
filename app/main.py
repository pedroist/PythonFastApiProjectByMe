from typing import Annotated, Generator
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models
from app.database import engine, SessionLocal
from app.models import Todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Todos).all()
