from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime
from sqlalchemy import UniqueConstraint
from enum import Enum as PyEnum
from sqlalchemy.sql import func
from app.database.database import Base

class ApplicationStatus(PyEnum):
    APPLIED = "applied"
    UNDER_REVIEW = "under_review"
    INTERVIEW = "interview"
    OFFER = "offer"
    REJECTED = "rejected"    



class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False, index=True)
    applicant_id = Column(Integer, ForeignKey("applicant_profiles.id"), nullable=False)

    __table_args__ = (
    UniqueConstraint("applicant_id", "job_id", name="unique_application_per_job"),
    )
    
    status = Column(Enum(ApplicationStatus), nullable=False, default=ApplicationStatus.APPLIED) # enum
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_updated_at = Column(DateTime(timezone=True), nullable=True)