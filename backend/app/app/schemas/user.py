from pydantic import Field

from app.schemas.base import BaseSchema


# Shared properties
class BaseUser(BaseSchema):
    email: str | None = Field(None, title="Адрес электронной почты")
    tel: str | None = Field(None, title="Номер телефона")
    is_active: bool | None = Field(True, title="Является ли аккаунт пользователя активным")
    is_superuser: bool = Field(False, title="Является ли пользователь администратором системы")
    full_name: str | None = Field(None, title="ФИО пользователя")
    city: str | None = Field(None, title="Город пользователя")


# Properties to receive via API on creation
class CreatingUser(BaseUser):
    password: str | None = Field(None, title="Постоянный пароль")


# Properties to receive via API on update
class UpdatingUser(BaseUser):
    password: str | None = Field(None, title="Постоянный пароль")


class GettingUser(BaseUser):
    id: int | None = Field(None, title="Идентификатор пользователя")
    last_activity: int | None = Field(None, title="время последнего запроса на сервер")
    high_school_request_count: int | None = Field(None, title="количество поданных заявок")
    avatar: str | None = Field(None, title="аватар")


class EmailPasswordBody(BaseSchema):
    email: str = Field(...,title="Адрес электронной почты")
    password: str = Field(...,title="Постоянный пароль")


class TelPasswordBody(BaseSchema):
    tel: str = Field(...,title="Номер телефона")
    password: str = Field(...,title="Постоянный пароль")


class TokenWithUser(BaseSchema):
    user: GettingUser = Field(..., title="Профиль пользователя")
    token: str = Field(...,title="Токен пользователя")


class ExistsRequest(BaseSchema):
    email: str | None = Field(None,title="Адрес электронной почты")


class ExistsResponse(BaseSchema):
    exists: bool = Field(None, title="Пользователь с хотя бы одним из переданных параметров существует")


class Registration(BaseSchema):
    code: str = Field(..., title="Код подтверждения")
    password: str = Field(..., title="Пароль")


class RegistrationByTel(Registration):
    tel: str = Field(..., title="Номер телефона")


class RegistrationByEmail(Registration):
    email: str = Field(..., title="Адрес электронной почты")
