from enum import Enum
from pathlib import Path
from pydantic import BaseModel
from app.models.document import DocumentState


class DocumentCreate(BaseModel):
    filename: str
    content_type: str
    path: Path
    owner_id: int

class DocumentUpdate(BaseModel):
    id: int
    filename: str
    content_type: str

class Document(BaseModel):
    id: int
    filename: str
    content_type: str
    path: str
    owner_id: int
    state: DocumentState

    class Config:
        orm_mode = True


class ConvertableFormats(str, Enum):
    ZIP = "zip"
    XML = "xml"

    PPTX = "pptx"
    ODT = "odt"
    XLS = "xls"
    DOCX = "docx"
