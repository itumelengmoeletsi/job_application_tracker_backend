from pydantic import BaseModel, Field 
from typing import Optional
from datetime import datetime
from enum import Enum

# Enum for API validation

class RecruiterPermissionLevel(str, Enum):
    ADMIN = "admin"
    SENIOR_RECRUITER = "senior_recruiter"
    RECRUITER = "recruiter"
    VIEWER = "viewer"

class RecruiterBase(BaseModel):
    department: str = Field(..., description="Department that recruiter works in.") 
    job_title: str = Field(..., description="Recruiter's job title")
    

class RecruiterCreate(RecruiterBase):
    permission_level: RecruiterPermissionLevel

class RecruiterUpdate(BaseModel): 
    department: Optional[str] = Field(default=None, max_length=50)
    job_title: Optional[str] = Field(default=None, max_length=100)
    internal_notes: Optional[str] = Field(default=None, max_length=255)

class DocumentResponse(RecruiterBase):
    id: int
    permission_level: RecruiterPermissionLevel
    internal_notes: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config: 
        from_attributes = True