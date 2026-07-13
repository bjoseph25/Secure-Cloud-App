from fastapi import FastAPI
from .database import engine
from .models import Base

from app.core.config import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Secure Cloud App API with FastAPI + PostgreSQL,",
            "status": "running"
    
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }