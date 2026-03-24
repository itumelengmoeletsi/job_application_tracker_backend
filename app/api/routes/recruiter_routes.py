from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.recruiter_schema import (RecruiterCreate, RecruiterResponse, RecruiterUpdate)
from app.services.recruiter_service import (create_recruiter, update_recruiter)

router = APIRouter(
    prefix="/recruiters",
    tags=["Recruiters"]
)

@router.post("/", response_model=RecruiterResponse, status_code=201)
def create_recruiter_route(
    recruiter: RecruiterCreate,
    db: Session = Depends(get_db)
):
    """Create a new recruiter profile"""
    try:
        new_recruiter = create_recruiter(db, recruiter)
        return new_recruiter
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{recruiter_id}", response_model=RecruiterResponse)
def update_recruiter_route(
    recruiter_id: int,
    recruiter: RecruiterUpdate,
    db: Session = Depends(get_db)
): 
    """Update recruiter information"""
    try:
        updated_recruiter = update_recruiter(db, recruiter_id, recruiter)
        return updated_recruiter
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))