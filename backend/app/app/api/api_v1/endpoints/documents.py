from typing import Any, List
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Body, Depends, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.core.celery_app import celery_app

router = APIRouter()


@router.post("/upload")
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
    document_serializer = schemas.Document.from_orm(document)
    celery_app.send_task("app.worker.check_file_type", args=[document_serializer.dict()])
    return document_serializer

@router.put("/{document_id}/upload")
def overwrite_document(
    document_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Overwrite document.
    """
    existing_document = crud.document.get(db, document_id)
    old_stem, _old_ext = existing_document.filename.rsplit(".", maxsplit=1)
    _new_stem, new_ext = file.filename.rsplit(".", maxsplit=1)
    new_document = schemas.DocumentUpdate(
        id=document_id,
        filename=f"{old_stem}.{new_ext}",
        content_type=file.content_type,
    )
    document = crud.document.update(db, db_obj=existing_document, obj_in=new_document, file=file.file)
    document_serializer = schemas.Document.from_orm(document)
    celery_app.send_task("app.worker.check_file_type", args=[document_serializer.dict()])
    return document_serializer

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


@router.post("/{document_id}/metadata", response_model=schemas.Metadata)
def add_document_metadata(
    document_id: int,
    metadata_s: schemas.Metadata,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """Add metadata to document"""
    document = crud.document.get(db, document_id)
    if document is None or document.owner_id != current_user.id:
        raise HTTPException(
            status_code=404, detail="The document was not found"
        )
    metadata_c = schemas.MetadataCreate(document_id=document_id, **metadata_s.dict())
    metadata_o = crud.metadata.create(db, obj_in=metadata_c)
    return metadata_o
