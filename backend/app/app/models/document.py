from typing import TYPE_CHECKING
from enum import Enum

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy import Enum as EnumSQL
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class DocumentState(str, Enum):
    UPLOADED = "uploaded"
    ACCEPT_CONVERSION = "accept_conversion"
    CONVERT = "convert"
    VALIDATE = "validate"
    ACCEPT_FIX = "accept_fix"
    FIX = "fix"


class Document(Base):
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    path = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    owner = relationship("User")
    state = Column(EnumSQL(DocumentState), default=DocumentState.UPLOADED, nullable=False)
