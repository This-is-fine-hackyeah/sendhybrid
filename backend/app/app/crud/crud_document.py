from typing import Any, Dict, Optional, Union
from pathlib import Path
import shutil

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.document import Document
from app.models.report import Report
from app.schemas.document import DocumentCreate, DocumentUpdate, Document as DocumentSer


class CRUDDocument(CRUDBase[Document, DocumentCreate, DocumentUpdate]):
    def create(self, db: Session, *, obj_in: DocumentCreate, file: Any) -> Document:
        path = Path(obj_in.path.parent)
        path.mkdir(parents=True, exist_ok=True)

        with open(obj_in.path, 'wb+') as out_file:
            shutil.copyfileobj(file, out_file)

        db_obj = Document(
            path=str(obj_in.path),
            report=Report(),
            **obj_in.dict(exclude={"path"})
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Document,
        obj_in: DocumentUpdate,
        file: Any
    ) -> Document:
        with open(db_obj.path, 'wb') as out_file:
            shutil.copyfileobj(file, out_file)

        update_data = obj_in.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def mark_failed(self, db: Session, *, validator_name: str, document_id: int):
        db_obj = self.get(db, document_id)
        setattr(db_obj.report, validator_name, False)
        db.add(db_obj.report)
        db.commit()

    def mark_passed(self, db: Session, *, validator_name: str, document_id: int):
        db_obj = self.get(db, document_id)
        setattr(db_obj.report, validator_name, True)
        db.add(db_obj.report)
        db.commit()

document = CRUDDocument(Document)
