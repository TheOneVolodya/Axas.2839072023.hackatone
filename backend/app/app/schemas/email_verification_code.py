import enum
from typing import Optional

from pydantic import Field
from app.schemas.base import BaseSchema


class CreatingEmailVerificationCode(BaseSchema):
    email: str = Field(..., title="Email")


class UpdatingEmailVerificationCode(BaseSchema):
    pass


class GettingEmailVerificationCode(BaseSchema):
    code: str = Field(..., title="Код подтверждения(только для тестов)")


class VerifyingEmailCode(BaseSchema):
    email: str = Field(..., title="Email")
    code: str = Field(..., title="Код подтверждения")
