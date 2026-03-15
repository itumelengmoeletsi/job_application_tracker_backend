from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional 

# Base Schema
# Shared fields between schemas

class JobBase(BaseModel):               
    title: str = Field(..., max_length=255)
    job_description: str

# Creat Schema
# Used when creating a job

class JobCreate(JobBase):
    pass

# Update Schema
# Used when updating a job

class JobUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=255)
    job_description: Optional[str] = None
    status: Optional[str] = None

# Response Schema
# Returned by the API

class JobResponse(JobBase):
    id: int
    status: str
    created_at: datetime
    closed_at: Optional[datetime] = None

    class Config:
        from_attributes = True # this allows sqlalchemy models to be converted into API responses