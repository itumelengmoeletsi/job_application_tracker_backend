from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, nullable=False)
    applicant_id = Column(Integer, ForeignKey("applicant_profiles.id"), nullable=False)
    file_url = Column(String(255), nullable=False)
    file_name = Column(String(50), nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    file_size = Column(Integer, nullable=False) 