from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas, deps, getters
from app.config import settings
from app.exceptions import UnprocessableEntity
from app.models import User
from app.utils import security
from app.utils.auth_session.schemas import AuthSessionInfo
from app.utils.auth_session.deps import get_auth_session_info, in_auth_session
from app.utils.logging import lprint
from app.utils.response import get_responses_description_by_codes

router = APIRouter()


def authenticate(
        db: Session,
        user: User | None,
        auth_session_info: AuthSessionInfo
):
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect login data")
    elif not user.is_active:
        raise HTTPException(status_code=401, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    session = crud.auth_session.create(db=db, obj_in={}, **auth_session_info.dict(), user=user,is_activate=True)
    print(session.id)

    return security.create_token(
        user.id,
        expires_delta=access_token_expires,
        token_type="access",
        session_id=session.id
    )


def validate_code(code):
    if code == -3:
        raise UnprocessableEntity(
            message='Код не отправлялся на этот номер телефона', num=0)
    if code == -1:
        raise UnprocessableEntity(
            message='Код уже использован', num=1)
    if code == -2:
        raise UnprocessableEntity(
            message='Время жизни кода истекло', num=2)
    if code == -4:
        raise UnprocessableEntity(
            message='Код подтверждения не совпадает', num=2)


@router.post(
    '/login/access-token',
    response_model=schemas.Token, tags=["Вход"],
    name="Войти по логину и паролю",
    responses=get_responses_description_by_codes([400, 401])
)
def login_access_token(
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends(),
        auth_session_info: AuthSessionInfo = Depends(get_auth_session_info)
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = crud.user.authenticate(
        db, email=form_data.username, password=form_data.password
    )

    return {
        'access_token': authenticate(db=db, user=user, auth_session_info=auth_session_info),
        'token_type': 'bearer',
    }


@router.post(
    '/sign/email-code/',
    response_model=schemas.response.SingleEntityResponse[schemas.user.TokenWithUser],
    name="Войти или зарегистрироваться по email и коду подтверждения",
    responses=get_responses_description_by_codes([400, 422, 403]),
    tags=["Вход"]
)
def sign_in(
        data: schemas.email_verification_code.VerifyingEmailCode,
        db: Session = Depends(deps.get_db),
        auth_session_info: AuthSessionInfo = Depends(get_auth_session_info)
):
    code = crud.crud_email_verification_code.email_verification_code.check_verification_code(
        db=db,
        data=data
    )

    validate_code(code)

    user = crud.crud_user.user.get_by_attrs(db=db, email=data.email, auto_create=True)

    return schemas.response.SingleEntityResponse(
        data=schemas.user.TokenWithUser(
            token=authenticate(db=db, user=user, auth_session_info=auth_session_info),
            user=getters.user.get_user(user)
        )
    )


@router.post(
    '/sign-out/',
    response_model=schemas.response.OkResponse,
    name="выйти",
    responses=get_responses_description_by_codes([400, 422, 403]),
    tags=["Вход"]
)
def sign_in(
        data: schemas.base.BaseSchema,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(in_auth_session(deps.get_current_active_user))
):

    user = crud.crud_user.user.sign_out(db=db, user=current_user)

    return schemas.response.OkResponse
