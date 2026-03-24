from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.job_schema import (JobCreate, JobUpdate, JobResponse)
from app.services.job_service import (create_job, update_job)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@router.post("/", response_model=JobResponse, status_code=201)
def create_job_route(
    job: JobCreate,
    db: Session = Depends(get_db)
):
    """Create job posting"""
    try:
        new_job = create_job(db, job)
        return new_job
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{job_id}", response_model=JobResponse)
def update_job_router(
    job_id: int,
    job: JobUpdate,
    db: Session = Depends(get_db)
):
    """Update job posting"""
    try:
        updated_job = update_job(db, job_id, job)
        return updated_job
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
