from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.StationBase])
def list_stations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stations = crud.get_stations(db, skip=skip, limit=limit)
    return stations

@router.get("/{station_id}", response_model=schemas.StationBase)
def get_station(station_id: str, db: Session = Depends(get_db)):
    station = crud.get_station(db, station_id=station_id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    return station