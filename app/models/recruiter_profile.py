from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Recruiter(Base):
    __tablename__ = "recruiter_profiles"

    id = Column(Integer, primary_key=True, index=True)
    department = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    permission_level = Column(String, nullable=False)
    interanal_notes = Column(String, nullable=True)