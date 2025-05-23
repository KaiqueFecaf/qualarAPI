from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from .database import Base

class Station(Base):
    __tablename__ = "stations"

    id = Column(String(10), primary_key=True)
    name = Column(String(100), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    region = Column(String(50))

class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(String(10), ForeignKey('stations.id'))
    parameter = Column(String(10))
    value = Column(Float)
    unit = Column(String(10))
    timestamp = Column(DateTime)
    quality_flag = Column(Integer)