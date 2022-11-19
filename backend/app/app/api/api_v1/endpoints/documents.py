from typing import Any, List
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.post("/upload", response_model=schemas.Document)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Upload document.
    """
    new_document = schemas.DocumentCreate(
        filename=file.filename,
        content_type=file.content_type,
        path=Path(settings.UPLOAD_DIR) / f"{uuid4()}_{file.filename}",
        owner_id=current_user.id
    )
    document = crud.document.create(db, obj_in=new_document, file=file.file)
    return document

@router.get("/{document_id}/download")
def download_document(
    document_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Download document.
    """
    document = crud.document.get(db, document_id)
    if document is None or document.owner_id != current_user.id:
        raise HTTPException(
            status_code=404, detail="The document was not found"
        )
    return FileResponse(document.path, media_type='application/octet-stream', filename=document.filename)
