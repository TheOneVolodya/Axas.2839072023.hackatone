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
    '/users/exists/',
    tags=[" Пользователи"],
    name="Проверить на существование пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.user.ExistsResponse],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def check_user(
        email: str | None = Query(None),
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user))
):
    exists = crud.crud_user.user.exists(db=db, data=schemas.user.ExistsRequest(email=email))

    return schemas.response.SingleEntityResponse(
        data=exists
    )


@router.get(
    '/users/me/',
    tags=[" Профиль"],
    name="Получить текущего пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.user.GettingUser],
    responses=get_responses_description_by_codes([401, 403])
)
def get_user_by_id(
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user)),
):
    return schemas.response.SingleEntityResponse(
        data=getters.user.get_user(user=current_user)
    )


@router.put(
    '/users/me/',
    tags=[" Профиль"],
    name="изменить текущего пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.user.GettingUser],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def edit_user(
        data: schemas.user.UpdatingUser,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user))
):
    user = crud.crud_user.user.update(db=db, db_obj=current_user, obj_in=data)

    return schemas.response.SingleEntityResponse(
        data=getters.user.get_user(user=user)
    )



@router.put(
    '/users/me/avatar/',
    tags=[" Профиль"],
    name="изменить аватар текущего пользователя",
    response_model=schemas.response.SingleEntityResponse[schemas.user.GettingUser],
    responses=get_responses_description_by_codes([401, 403, 400])
)
def edit_user_avatar(
        new_avatar: UploadFile | None = File(None),
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user))
):
    crud.crud_user.user.change_avatar(db=db,user=current_user,new_avatar=new_avatar)

    return schemas.response.SingleEntityResponse(
        data=getters.user.get_user(user=current_user)
    )


@router.delete(
    '/users/me/',
    tags=[" Профиль"],
    name="удалить текущего пользователя",
    response_model=schemas.response.OkResponse,
    responses=get_responses_description_by_codes([401, 403])
)
def del_user(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user))
):
    crud.crud_user.user.remove_obj(db=db, obj=current_user)
    return schemas.response.OkResponse()


@router.get(
    '/users/me/sessions/',
    tags=[" Профиль"],
    name="Получить сеансы пользователя по идентификатору",
    response_model=schemas.response.ListOfEntityResponse[GettingAuthSession],
    responses=get_responses_description_by_codes([401, 403, 400, 404])
)
def get_auth_session_by_user_id(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user)),
        page: int | None = Query(None)
):

    user = current_user
    is_current = True

    data, paginator = crud.auth_session.get_page(db=db, page=page, user_id=user.id, is_ended=False)

    return schemas.response.ListOfEntityResponse(
        data=[
            getters.get_auth_session(auth_session=auth_session, user=user if is_current else None)
            for auth_session in data
        ],
        meta=schemas.response.Meta(paginator=paginator)
    )


@router.delete(
    '/users/sessions/{session_id}/',
    tags=[" Профиль"],
    name="Удалить сеанс пользователя",
    response_model=schemas.response.OkResponse,
    responses=get_responses_description_by_codes([401, 403, 400])
)
def del_session(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user)),
        session_id: int = Path(...),
):
    crud.auth_session.remove_by_id(db=db, id=session_id)

    return schemas.response.OkResponse()



