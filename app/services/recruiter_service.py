from sqlalchemy.orm import Session
from app.models.recruiter_profile import Recruiter
from app.schemas.recruiter_schema import RecruiterCreate, RecruiterUpdate

def create_recruiter(db: Session, recruiter_data: RecruiterCreate):
    # Create recruiter profile
    new_recruiter = Recruiter(
        department=recruiter_data.department,
        job_title=recruiter_data.job_title,
        permission_level=recruiter_data.permission_level.upper()
    )

    # Save to database
    db.add(new_recruiter)
    db.commit()
    db.refresh(new_recruiter)

    return new_recruiter

def update_recruiter(db: Session, recruiter_id: int, recruiter_data: RecruiterUpdate):
    # Fetch recruiter
    recruiter = db.query(Recruiter).filter(Recruiter.id == recruiter_id).first()

    if not recruiter:
        raise ValueError("Recruiter not found")
    
    # Update fields only if provided
    if recruiter_data.department is not None:
        recruiter.department = recruiter_data.department
    
    if recruiter_data.job_title is not None:
        recruiter.job_title = recruiter_data.job_title
    
    if recruiter_data.internal_notes is not None:
        recruiter.internal_notes = recruiter_data.internal_notes

    # Save changes
    try: 
        db.commit()
    except Exception:
        db.rollback()
        raise
    db.refresh(recruiter)

    return recruiter

# TODO: Maybe add a delete service for when a recruiter decides to leave the company