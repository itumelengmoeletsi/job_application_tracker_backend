from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.application_schema import (ApplicationCreate, ApplicationStatusUpdate, ApplicationResponse)
from app.services.application_service import (apply_to_job)

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

@router.post("/", response_model=ApplicationResponse, status_code=201)
def create_application_route(
    application: ApplicationCreate,
    db: Session = Depends(get_db)
):
    """Creates a new application"""
    try:
        new_application = apply_to_job(db, application)
        return new_application
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))