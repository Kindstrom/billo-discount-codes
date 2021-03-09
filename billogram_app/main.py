from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas, helpers
from .database import SessionLocal, engine

import random

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Billogram Discount Codes",
    description="Fredrik Kindströms API",
    version="1.0.0"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/discount_codes/generate_codes/{brand_id}")
def create_discount_codes(
    brand_id: int,
    no_of_codes: int = 10,
    db: Session = Depends(get_db)
):
    codes = helpers.generate_discount_codes(no_of_codes)
    for code in codes:
        crud.create_discount_code(db=db, code=code, brand_id=brand_id)
    return codes


@app.get("/discount_codes/get_code/{brand_id}", response_model=schemas.DiscountCode)
def get_discount_code(brand_id: int, db: Session = Depends(get_db)):
    db_discount_code = crud.get_discount_code(db=db, brand_id=brand_id)
    if db_discount_code is None:
        raise HTTPException(status_code=404, detail='This brand has no created discount codes!')
    return db_discount_code
