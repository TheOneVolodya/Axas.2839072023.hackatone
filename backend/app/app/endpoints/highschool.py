from typing import Literal

from fastapi import APIRouter, Query, Depends, Path, UploadFile, File
from sqlalchemy.orm import Session

from app import crud, schemas, getters, deps, models
from app.exceptions import UnfoundEntity
from app.utils.auth_session.deps import in_auth_session
from app.utils.auth_session.schemas import GettingAuthSession
from app.utils.response import get_responses_description_by_codes

from app.utils.logging import lprint

router = APIRouter()


@router.get(
    '/highschool/',
    tags=["Вузы"],
    name="Получить все вузы",
    response_model=schemas.response.ListOfEntityResponse[schemas.GettingHighSchool],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_highschools(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user)),
        name: str | None = Query(None),
        is_gov: bool | None = Query(None),
        has_military_dep: bool | None = Query(None),
        page: int | None = Query(None)
):

    data, paginator = crud.crud_highschool.highschool.get_page(
        db=db,
        page=page,
        name=name,
        is_gov=is_gov,
        has_military_dep=has_military_dep
    )

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.get_high_school(hs)
            for hs in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )
