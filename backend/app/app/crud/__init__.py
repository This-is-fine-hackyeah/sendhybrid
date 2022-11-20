from .crud_item import item
from .crud_user import user
from .crud_settings import settings
from .crud_document import document
from .crud_report import report

from .base import CRUDBase
from app.models.report import Metadata
from app.schemas.report import Metadata as MetadataS
from app.schemas.report import MetadataCreate

metadata = CRUDBase[Metadata, MetadataCreate, MetadataS](Metadata)
