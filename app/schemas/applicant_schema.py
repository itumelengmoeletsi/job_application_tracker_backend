from pydantic import BaseModel, Field 
from typing import Optional

class ApplicantBase(BaseModel):
    phone_number: str = Field(..., max_length=20)
    cv_url: str = Field(..., max_length=200)
    experience_summary: str = Field(..., max_length=2000)
    
class ApplicantCreate(ApplicantBase):
    pass

# did not inherit parent base because update feature should allow partial modificaiton
# class ApplicantUpdate(ApplicantBase) would force required fields
class ApplicantUpdate(BaseModel):
    phone_number: Optional[str] = Field(default=None, max_lenght=20)
    cv_url: Optional[str] = Field(default=None, max_length=255)
    experience_summary: Optional[str] = Field(default=None, max_length=2000)

class ApplicantResponse(ApplicantBase):
    id: int


    class Config:
        from_attributes = True