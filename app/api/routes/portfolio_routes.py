from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.portfolio_schema import (PortfolioLinkCreate, PortfolioLinkUpdate, PortfolioLinkResponse)
from app.services.portfolio_service import (create_portfolio_link, update_portfolio_link)

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)

@router.post("/", response_model=PortfolioLinkResponse, status_code=201)
def create_portfolio_link_router(
    portfolio_link: PortfolioLinkCreate,
    db: Session = Depends(get_db)
):
    """Paste link"""
    try:
        new_link = create_portfolio_link(db, portfolio_link)
        return new_link
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{portfolio_link_id}", response_model=PortfolioLinkResponse)
def update_portfolio_link_router(
    portfolio_link_id: int,
    portfolio_link: PortfolioLinkUpdate,
    db: Session = Depends(get_db)
):
    """Update link"""
    try:
        updated_link = update_portfolio_link(db, portfolio_link_id, portfolio_link)
        return updated_link
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))