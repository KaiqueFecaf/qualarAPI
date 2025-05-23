from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.post("/query", response_model=List[schemas.MeasurementBase])
def query_measurements(
    query: schemas.MeasurementQuery,
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 1000
):
    measurements = crud.get_measurements(db, query=query, skip=skip, limit=limit)
    if not measurements:
        raise HTTPException(status_code=404, detail="No measurements found")
    return measurements