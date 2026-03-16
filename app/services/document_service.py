from sqlalchemy.orm import Session
from app.models.document import Document
from app.schemas.document_schema import DocumentCreate, DocumentUpdate

def upload_document(db: Session, document_data: DocumentCreate):
    new_document = Document(
        applicant_id=document_data.applicant_id,
        file_url=str(document_data.file_url),
        file_name=document_data.file_name, 
        file_size=document_data.file_size
    )

    db.add(new_document)
    try: 
        db.commit()
    except Exception:
        db.rollback()
        raise
    db.refresh(new_document)

    return new_document

def update_document(db: Session, document_id: int, document_data: DocumentUpdate):
    document = db.query(Document).filter(Document.id == document_id).first()

    if not document:
        raise ValueError("Document not found.")
    
    update_data = document_data.model_dump(exclude_unset=True)
    
    if "file_url" in update_data:
        update_data["file_url"] = str(update_data["file_url"])

    for field, value in update_data.items():
        setattr(document, field, value)
    
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    db.refresh(document)

    return document