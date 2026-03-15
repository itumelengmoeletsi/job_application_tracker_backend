from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

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
# Applicatino Status Update Schema
# ---------------------------------------
# Only recruiters should use this
# It updates the workflow state of the application

class ApplicationStatusUpdate(BaseModel):
    status: str = Field(..., description="New workflow state for the application")

    # Possible values might late include:
    # applied 
    # under_review
    # interview
    # offer
    # rejected

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
    updated_at: datetime

    class Config:
        from_attributes = True