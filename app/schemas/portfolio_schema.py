from pydantic import BaseModel, Field, HttpUrl
from typing import Optional 

class PortfolioLinkBase(BaseModel):
    url: HttpUrl = Field(..., description="Link to Portfolio projects")
    label: str = Field(..., description="Name of the project")

class PortfolioLinkCreate(PortfolioLinkBase):
    applicant_id: int = Field(..., description="Applicant who linked the project")

class PortfolioLinkUpdate(BaseModel):
    url: Optional[HttpUrl] = None
    label: Optional[str] = Field(default=None, max_length=100)

class PortfolioLinkResponse(PortfolioLinkBase):
    id: int
    applicant_id: int

    class Config:
        from_attributes = True

