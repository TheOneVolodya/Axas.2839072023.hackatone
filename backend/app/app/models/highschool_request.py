from typing import Any
from datetime import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel
from app.utils.auth_session.models import AuthSessionMixin


class HighschoolRequest(BaseModel):
    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime, nullable=True, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    high_school_id = Column(Integer, ForeignKey('highschool.id'), nullable=True)
    status = Column(String, nullable=False,default="ожидает подачи документов")

    user = relationship('User', back_populates='requests')
    high_school = relationship('Highschool', back_populates='requests')
