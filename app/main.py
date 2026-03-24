from fastapi import FastAPI
from app.database.database import engine, Base 
from app import models

# Import routers
from app.api.routes import applicant_routes
from app.api.routes import application_routes
from app.api.routes import document_routes
from app.api.routes import job_routes
from app.api.routes import portfolio_routes
from app.api.routes import recruiter_routes


app = FastAPI(
    title = "Job Application Tracker API",
    version = "1.0.0"
)

# Create Tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "API is running",
        "version": "1.0.0",
        "available_routes": [
            "/applcants",
            "/aocuments",
            "/jobs",
            "/popplications",
            "/portfolio_links",
            "/recruiters"
        ]
    }

# Register routes
API_PREFIX = "/api"

app.include_router(applicant_routes.router, prefix=API_PREFIX)
app.include_router(application_routes.router, prefix=API_PREFIX)
app.include_router(document_routes.router, prefix=API_PREFIX)
app.include_router(job_routes.router, prefix=API_PREFIX)
app.include_router(portfolio_routes.router, prefix=API_PREFIX)
app.include_router(recruiter_routes.router, prefix=API_PREFIX)