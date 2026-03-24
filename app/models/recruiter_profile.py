from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy import Enum
from enum import Enum as PyEnum
from app.database.database import Base

class RecruiterPermissionLevel(PyEnum):
    ADMIN = "admin"
    SENIOR_RECRUITER = "senior_recruiter"
    RECRUITER = "recruiter"
    VIEWER = "viewer"

class Recruiter(Base):
    __tablename__ = "recruiter_profiles"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String(50), nullable=False)
    job_title = Column(String(100), nullable=False)
    permission_level = Column(
        Enum(RecruiterPermissionLevel, native_enum=False),
        nullable=False,
        default=RecruiterPermissionLevel.RECRUITER
    )
    internal_notes = Column(String(255), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())