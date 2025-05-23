from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import stations, measurements

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CETESB Air Quality API",
    description="API for accessing air quality data from CETESB",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(stations.router, prefix="/api/v1/stations", tags=["stations"])
app.include_router(measurements.router, prefix="/api/v1/measurements", tags=["measurements"])