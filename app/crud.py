from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def get_station(db: Session, station_id: str):
    return db.query(models.Station).filter(models.Station.id == station_id).first()

def get_stations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Station).offset(skip).limit(limit).all()

def get_measurements(
    db: Session,
    query: schemas.MeasurementQuery,
    skip: int = 0,
    limit: int = 1000
):
    q = db.query(models.Measurement).filter(
        models.Measurement.station_id.in_(query.station_ids),
        models.Measurement.parameter.in_(query.parameters),
        models.Measurement.timestamp >= query.start_date,
        models.Measurement.timestamp <= query.end_date
    )
    
    if query.aggregate:
        # Implement aggregation logic here
        pass
        
    return q.order_by(models.Measurement.timestamp).offset(skip).limit(limit).all()