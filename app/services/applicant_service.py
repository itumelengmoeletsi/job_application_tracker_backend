from sqlalchemy.orm import Session
from app.models.applicant_profile import Applicant
from app.schemas.applicant_schema import ApplicantCreate, ApplicantUpdate

def create_applicant(db: Session, applicant_data: ApplicantCreate):
    # Create applicant profile
    new_applicant = Applicant(
        phone_number=applicant_data.phone_number,
        cv_url=applicant_data.cv_url,
        experience_summary=applicant_data.experience_summary
    )

    # Save to database
    db.add(new_applicant)
    try: 
        db.commit()
    except Exception:
        db.rollback()
        raise
    db.refresh(new_applicant)

    return new_applicant

def update_applicant(db: Session, applicant_id: int, applicant_data: ApplicantUpdate):
    # Fetch applicant
    applicant = db.query(Applicant).filter(Applicant.id == applicant_id).first()

    if not applicant:
        raise ValueError("Applicant not found")
    
    update_data = applicant_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(applicant, key, value)
    
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise
    
    db.refresh(applicant)

    return applicant