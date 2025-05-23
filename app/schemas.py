from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class StationBase(BaseModel):
    id: str
    name: str
    latitude: Optional[float]
    longitude: Optional[float]
    region: Optional[str]

    class Config:
        orm_mode = True

class MeasurementBase(BaseModel):
    station_id: str
    parameter: str
    value: float
    unit: str
    timestamp: datetime
    quality_flag: Optional[int] = None

    class Config:
        orm_mode = True

class MeasurementQuery(BaseModel):
    station_ids: list[str]
    parameters: list[str]
    start_date: datetime
    end_date: datetime
    aggregate: Optional[str] = None  # 'hourly', 'daily', 'monthly'