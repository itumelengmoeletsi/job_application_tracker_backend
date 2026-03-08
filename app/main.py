from fastapi import FastAPI
from app.database.database import engine, Base
from app import models

app = FastAPI(
    title = "Job Application Tracker API",
    version = "1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running"}