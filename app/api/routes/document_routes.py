from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.document_schema import (DocumentCreate, DocumentUpdate, DocumentResponse)
from app.services.document_service import (upload_document, update_document)

router = APIRouter(
    prefix="/documents",
    tags=['Documents']
)

@router.post("/", response_model=DocumentResponse, status_code=201)
def create_document_route(
    document: DocumentCreate,
    db: Session = Depends(get_db)
):
    """Upload a documnet"""
    try:
        new_document = upload_document(db, document)
        return new_document
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{document_id}", response_model=DocumentResponse)
def update_document_route(
    document_id: int,
    document: DocumentUpdate,
    db: Session = Depends(get_db)
):
    """Update a document"""
    try:
        updated_document = update_document(db, document_id, document)
        return updated_document
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))