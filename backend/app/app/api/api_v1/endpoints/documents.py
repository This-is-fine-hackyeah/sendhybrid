from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.post("/upload", response_model=schemas.Document)
def upload_document(
    file: UploadFile,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Upload document.
    """
    new_document = schemas.DocumentCreate(
        filename=file.filename,
        content_type=file.content_type,
        path=Path(settings.UPLOAD_DIR) / file.filename,
        owner_id=current_user.id
    )
    document = crud.document.create(db, new_document, file.file)
    return document
