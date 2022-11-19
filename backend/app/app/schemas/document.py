from pathlib import Path
from pydantic import BaseModel


class DocumentCreate(BaseModel):
    filename: str
    content_type: str
    path: Path
    owner_id: int

class DocumentUpdate(BaseModel):
    pass

class Document(BaseModel):
    id: int
    filename: str
    content_type: str
    path: str
    owner_id: int

    class Config:
        orm_mode = True
