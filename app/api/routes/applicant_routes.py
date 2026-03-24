from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.applicant_schema import (ApplicantCreate, ApplicantUpdate, ApplicantResponse)
from app.services.applicant_service import (create_applicant, update_applicant)

router = APIRouter(
    prefix="/applicants",
    tags=["Applicants"]
)

@router.post("/", response_model=ApplicantResponse, status_code=201)
def create_applicant_route(
    applicant: ApplicantCreate,
    db: Session = Depends(get_db)
):
    """Creates a new applicant profile."""
    try:
        new_applicant = create_applicant(db, applicant)
        return new_applicant
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.patch("/{applicant_id}", response_model=ApplicantResponse)
def update_applicant_route(
    applicant_id: int,
    applicant: ApplicantUpdate,
    db: Session = Depends(get_db)
): 
    """Updates an applicant profile."""
    try:
        updated_applicant = update_applicant(db, applicant_id, applicant)
        return updated_applicant
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))