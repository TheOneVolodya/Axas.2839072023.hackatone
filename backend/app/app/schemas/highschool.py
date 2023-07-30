from pydantic import Field

from app.schemas.base import BaseSchema


# Shared properties
class BaseHighSchool(BaseSchema):
    name: str | None = Field(None, title="Название университета")
    lat: float | None = Field(None, title="Широта")
    lon: float | None = Field(None, title="Долгота")
    faculty_page: str | None = Field(None, title="Страница факультетов")
    home_page: str | None = Field(None, title="Домашняя страница университета")
    average_grade: int | None = Field(None, title="Средний бал поступления")
    top_position: int | None = Field(None, title="Место в топе")
    rate: int | None = Field(None, title="Оценка")


class CreatingHighSchool(BaseHighSchool):
    budget_place_count: int = Field(..., title="Количество бюджетных мест")
    is_gov: bool = Field(..., title="Является ли вуз государственным")
    has_military_dep: bool = Field(..., title="Имеет ли вуз военную кафедру")
    min_price: int = Field(..., title="Минимальная цена обучения (в год)")
    max_price: int = Field(..., title="Максимальная цена за обучение (в год)")
    study_area_count: int = Field(..., title="Количество направлений обучения")


class UpdatingHighSchool(BaseHighSchool):
    budget_place_count: int | None = Field(None, title="Количество бюджетных мест")
    is_gov: bool | None = Field(None, title="Является ли вуз государственным")
    has_military_dep: bool | None = Field(None, title="Имеет ли вуз военную кафедру")
    min_price: int | None = Field(None, title="Минимальная цена обучения (в год)")
    max_price: int | None = Field(None, title="Максимальная цена за обучение (в год)")
    study_area_count: int | None = Field(None, title="Количество направлений обучения")


class GettingHighSchool(BaseHighSchool):
    id: int = Field(..., title="Идентификатор вуза")
    budget_place_count: int = Field(..., title="Количество бюджетных мест")
    is_gov: bool = Field(..., title="Является ли вуз государственным")
    has_military_dep: bool = Field(..., title="Имеет ли вуз военную кафедру")
    min_price: int = Field(..., title="Минимальная цена обучения (в год)")
    max_price: int = Field(..., title="Максимальная цена за обучение (в год)")
    study_area_count: int = Field(..., title="Количество направлений обучения")