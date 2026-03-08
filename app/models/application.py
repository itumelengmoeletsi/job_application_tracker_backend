from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False, index=True)
    applicant_id = Column(Integer, ForeignKey("applicant_profiles.id"), nullable=False)
    status = Column(Boolean, nullable=False)
    last_updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)