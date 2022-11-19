from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email

router = APIRouter()


@router.get("/", response_model=schemas.Settings)
def get_settings(
    db: Session = Depends(deps.get_db),
):
    ret = crud.settings.get_or_create(db)
    print(ret)
    return schemas.Settings.from_orm(ret)


@router.put("/", response_model=schemas.Settings)
def update_settings(
    new_settings: schemas.SettingsUpdate,
    db: Session = Depends(deps.get_db),
    _current_user: models.User = Depends(deps.get_current_active_superuser),
):
    # get any settings
    settings_obj = crud.settings.get_or_create(db)
    updated = crud.settings.update(db, db_obj=settings_obj, obj_in=new_settings)
    return updated
