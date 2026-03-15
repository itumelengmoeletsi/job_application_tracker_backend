from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False, index=True)
    applicant_id = Column(Integer, ForeignKey("applicant_profiles.id"), nullable=False, unique=True)
    status = Column(String, nullable=False, default="applied")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_updated_at = Column(DateTime(timezone=True), nullable=True)