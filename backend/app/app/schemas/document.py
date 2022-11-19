from pydantic import BaseModel
from app import schemas


class DocumentCreate(BaseModel):
    filename: str
    content_type: str
    path: str
    owner_id: int

class DocumentUpdate(BaseModel):
    pass
