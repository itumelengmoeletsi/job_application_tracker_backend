from sqlalchemy.orm import Session
from datetime import datetime
from app.models.job import Job
from app.schemas.job_schema import JobCreate, JobUpdate

def create_job(db: Session, job_data: JobCreate):
    # Create job
    new_job = Job(
        title=job_data.title,
        description=job_data.description,
        status="OPEN"
    )

    # Save to db
    db.add(new_job)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    db.refresh(new_job)

    return new_job

def update_job(db: Session, job_id: int, job_data: JobUpdate):
    # Fetch job
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise ValueError("Job does not exist")
    
    if job_data.title is not None:
        job.title = job_data.title
    
    if job_data.description is not None:
        job.description = job_data.description
    
    if job_data.status is not None:
        job.status = job_data.status.upper()

        if job_data.status == "closed":
            job.closed_at = datetime.utcnow()
    
    # save to db
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    db.refresh(job)

    return job