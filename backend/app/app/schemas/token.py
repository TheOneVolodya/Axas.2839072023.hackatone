from app.schemas.base import BaseSchema
from pydantic import Field


class Token(BaseSchema):
    access_token: str = Field(...,title="токен доступа")
    token_type: str = Field(...,title="тип токена")


class TokenPayload(BaseSchema):
    sub: int | None = Field(None, title="идентификатор пользователя, которому выдан токен")
