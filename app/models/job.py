from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from enum import Enum as PyEnum
from app.database.database import Base

class JobStatus(PyEnum):
    OPEN = "open"
    CLOSED = "closed"

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(JobStatus), nullable=False, default=JobStatus.OPEN)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    closed_at = Column(DateTime(timezone=True), nullable=True)