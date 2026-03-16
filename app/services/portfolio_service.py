from sqlalchemy.orm import Session
from app.models.portfolio_links import PortfolioLink
from app.schemas.portfolio_schema import PortfolioLinkCreate, PortfolioLinkUpdate

def create_portfolio_link(db: Session, portfolio_data: PortfolioLinkCreate):
    new_portfolio_link = PortfolioLink(
        applicant_id=portfolio_data.applicant_id,
        url=str(portfolio_data.url),
        label=portfolio_data.label
    )

    db.add(new_portfolio_link)
    try: 
        db.commit()
    except Exception:
        db.rollback()
        raise
    db.refresh(new_portfolio_link)

    return new_portfolio_link

def update_portfolio_link(db: Session, portfolio_id: int, portfolio_data: PortfolioLinkUpdate):
    portfolio = db.query(PortfolioLink).filter(PortfolioLink.id == portfolio_id).first()

    if not portfolio:
        raise ValueError("Portfolio not found")
    
    update_data = portfolio_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        if key == "url":
            value = str(value)
        setattr(portfolio, key, value)

    try: 
        db.commit()
    except Exception:
        db.rollback()
        raise        
    db.refresh(portfolio)

    return portfolio
