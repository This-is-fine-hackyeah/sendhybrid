from typing import Any, Dict, Optional, Union
from pathlib import Path
import shutil

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentUpdate


class CRUDDocument(CRUDBase[Document, DocumentCreate, DocumentUpdate]):
    def create(self, db: Session, *, obj_in: DocumentCreate, file: Any) -> Document:
        path = Path(obj_in.path)
        path.mkdir(parents=True, exist_ok=True)

        with open(path, 'wb+') as out_file:
            shutil.copyfileobj(file, out_file)

        db_obj = Document(
            **obj_in.dict()
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


document = CRUDDocument(Document)
