from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Applicant(Base): 
    __tablename__ = "applicant_profiles"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(Integer, unique=True, nullable=False)
    cv_reference = Column(String, nullable=False)
    portfolio_link = Column(String, nullable=True) 
    experience_summary = Column(String, nullable=False)