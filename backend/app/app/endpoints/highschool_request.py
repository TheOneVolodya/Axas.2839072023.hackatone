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
    '/highschool/requested/',
    tags=["Вузы"],
    name="Получить все заявки в ВУЗы",
    response_model=schemas.response.ListOfEntityResponse[schemas.GettingHighschoolRequest],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_highschool_requests(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user)),
        page: int | None = Query(None)
):

    data, paginator = crud.crud_highschool_request.highschool_request.get_page(
        db=db,
        page=page,
        user_id=current_user.id
    )

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.get_highschool_request(hsr)
            for hsr in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.post(
    '/highschool/requested/',
    tags=["Вузы"],
    name="Подать заявление в вуз",
    response_model=schemas.response.SingleEntityResponse[schemas.GettingHighschoolRequest],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_highschool_requests(
        data: schemas.highschool_request.CreatingHighschoolRequest,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user)),
):

    hsr = crud.crud_highschool_request.highschool_request.create(
        db=db,
        obj_in=data,
        user_id=current_user.id
    )

    return schemas.response.SingleEntityResponse(
        data=getters.get_highschool_request(hsr),
        meta=schemas.response.Meta(paginator=None)
    )
