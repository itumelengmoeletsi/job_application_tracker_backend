from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class ApplicationStatus(str, Enum):
    APPLIED = "applied"
    UNDER_REVIEW = "under_review"
    INTERVIEW = "interview"
    OFFER = "offer"
    REJECTED = "rejected"

# ----------------------------------------
# Application Creation Schema
# ----------------------------------------
# Used when an applicant applies to a job.
# Notice that "status" is NOT included here.
# The system should automatically set status = "applied"
# Applicants are not allowed to control workflow state. 

class ApplicationCreate(BaseModel):
    job_id: int = Field(..., description="The job being applied to")

    #TODO: The following should come from authentication
    # (current logged-in user), but since auth is not built yet
    # it is included here
    applicant_id: int = Field(..., description="Applicant submitting the application") 


# ---------------------------------------
# Application Status Update Schema
# ---------------------------------------
# Only recruiters should use this
# It updates the workflow state of the application

class ApplicationStatusUpdate(BaseModel):
    status: Optional[str] = None

# --------------------------------------
# Application Response Schema
# --------------------------------------
# Used when returning application data to the client
# Includes system-generated fields like timestamsp

class ApplicationResponse(BaseModel):
    id: int
    job_id: int
    applicant_id: int
    status: str
    created_at: datetime
    last_updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True