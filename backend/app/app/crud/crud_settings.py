from app.crud.base import CRUDBase

from sqlalchemy.orm import Session
from app.models.settings import Settings
from app.schemas.settings import SettingsUpdate
from app.schemas.settings import Settings as SettingsS


class CRUDSettings(CRUDBase[Settings, SettingsS, SettingsUpdate]):
    def get_or_create(self, db: Session) -> Settings:
        setts = self.get_multi(db)
        if setts:
            return setts[-1]
        # create default
        db_obj = Settings()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


settings = CRUDSettings(Settings)
