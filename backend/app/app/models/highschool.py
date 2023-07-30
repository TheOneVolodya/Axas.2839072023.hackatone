from typing import Any

from sqlalchemy import Boolean, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel
from app.utils.auth_session.models import AuthSessionMixin


class Highschool(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    lat = Column(Float,nullable=True)
    lon = Column(Float,nullable=True)
    min_price = Column(Integer, nullable=False)
    max_price = Column(Integer, nullable=False)
    cover = Column(String, nullable=True)
    faculty_page = Column(String, nullable=True)
    home_page = Column(String, nullable=True)
    average_grade = Column(Integer, nullable=True)
    top_position = Column(Integer, nullable=True)
    rate = Column(Integer, nullable=True)
    budget_place_count = Column(Integer, nullable=False, default=0)
    is_gov = Column(Boolean, nullable=False, default=False)
    has_military_dep = Column(Boolean, nullable=False, default=False)
    study_area_count = Column(Integer, nullable=False, default=0)

    requests = relationship('HighschoolRequest', back_populates='high_school')