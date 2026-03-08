from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class PortfolioLink(Base):
    __tablename__ = "portfolio_links"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    applicant = Column(Integer, ForeignKey("applicant_profiles.id"), nullable=False, index=True)
    url = Column(String, nullable=True)
    label = Column(String, nullable=True)
    