from pydantic import Field

from app.schemas.base import BaseSchema
from app.schemas.highschool import GettingHighSchool

class CreatingHighschoolRequest(BaseSchema):
    user_id: int
    highschool_id: int


class UpdatingHighschoolRequest(BaseSchema):
    ...


class GettingHighschoolRequest(BaseSchema):
    id: int = Field(...,title="Идентификатор запроса")
    status: str = Field(..., title="Статус запроса")
    highschool: GettingHighSchool = Field(...,title="Вуз")

