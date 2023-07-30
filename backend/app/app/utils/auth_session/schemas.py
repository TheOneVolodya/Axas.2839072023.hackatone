from pydantic import Field
from app.schemas.base import BaseSchema


class AuthSessionInfo(BaseSchema):
    ip_address: str | None = Field(None, title="IP адрес")
    accept_language: str | None = Field(None, title="Языки клиента")
    user_agent: str | None = Field(None, title="Данные клиента")
    detected_os: str | None = Field(None, title="Операционная система клиента")
    firebase_token: str | None = Field()


class CreatingAuthSession(BaseSchema):
    pass


class UpdatingAuthSession(BaseSchema):
    pass


class GettingAuthSession(AuthSessionInfo):
    id: int = "Идентификатор сессии"
    created: int = Field(...,title="Время создания сессии(unix) ")
    ended: int | None = Field(None,title="Время окончания сессии(unix)")
    last_activity: int = Field(None,title="Время последнего действия в рамках этой сессии")
    is_current: bool | None = Field(None, title="Совершен ли запрос в мамках этой сессии")
