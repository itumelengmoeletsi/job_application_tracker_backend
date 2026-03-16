from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class PortfolioLink(Base):
    __tablename__ = "portfolio_links"

    id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicant_profiles.id"), nullable=False, index=True)
    url = Column(String(255), nullable=False)
    label = Column(String(100), nullable=False)
    