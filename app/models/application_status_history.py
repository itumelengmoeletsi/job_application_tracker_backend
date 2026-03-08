from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class AppStatHistory(Base):
    __tablename__ = "application_status_history"

    id = Column(Integer, primary_key=True, nullable=False)
    applicaiton_id = Column(Integer, ForeignKey("applications.id"), nullable=False)
    status = Column(Boolean, nullable=False)
    applied_at = Column(DateTime(timezone=True), server_default=func.now())
    last_updated = Column(DateTime(timezone=True), nullable=True) 