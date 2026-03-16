from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from typing import Optional

class DocumentBase(BaseModel):
    file_url: HttpUrl = Field(..., description="Location of the uploaded document")
    file_name: str = Field(..., max_length=50, description="Original file name")
    file_size: int = Field(..., description="File size in bytes")

class DocumentCreate(DocumentBase):
    applicant_id: int = Field(..., description="Applicant who uploaded the document")

# Documents are often immutable, but if 
# i decide to allow updates this schema enables
# partial updates

class DocumentUpdate(BaseModel):
    file_url: Optional[HttpUrl] = None
    file_name: Optional[str] = Field(default=None, max_length=50)
    file_size: Optional[int] = None

# response schemas should only add fields not already defined in the base schema
class DocumentResponse(DocumentBase):
    id: int
    applicant_id: int
    uploaded_at: datetime

    class Config:
        from_attributes = True
