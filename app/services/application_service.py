from sqlalchemy.orm import Session
from app.models.application import Application
from app.models.job import Job
from app.schemas.application_schema import ApplicationCreate

def apply_to_job(db: Session, application_data: ApplicationCreate):
    # Check if the job exists
    job = db.query(Job).filter(Job.id == application_data.job_id).first()
    if not job:
        raise ValueError("Job does not exist")
    
    # Prevent duplicate applications
    existing_application = db.query(Application).filter(
        Application.job_id == application_data.job_id,
        Application.applicant_id == application_data.applicant_id
    ).first()

    if existing_application:
        raise ValueError("Applicant has already applied to this job")
    
    # Create new application
    new_application = Application(
        job_id=application_data.job_id,
        applicant_id=application_data.application_id,
        status="applied"
    )

    # Save to database 
    db.add(new_application)
    try:
        db.commit()
    except Exception():
        db.rollback()
        raise

    db.refresh(new_application)

    return new_application