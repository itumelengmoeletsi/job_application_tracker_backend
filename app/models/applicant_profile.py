from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Applicant(Base): 
    __tablename__ = "applicant_profiles"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(20), unique=True, index=True, nullable=False)
    cv_url = Column(String, nullable=False) 
    experience_summary = Column(String(2000), nullable=False)