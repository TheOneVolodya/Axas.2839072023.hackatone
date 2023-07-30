from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union

from sqlalchemy import desc, orm
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.highschool import Highschool
from app.schemas.base import BaseSchema
from app.schemas.highschool import CreatingHighSchool, UpdatingHighSchool
from app.utils.code import fake_gen


class CRUDHighSchool(CRUDBase[Highschool, CreatingHighSchool, UpdatingHighSchool]):
    def _get_filter_by_name(self, name):
        match name:
            case 'name':
                return lambda query, value: query.filter(self.model.name.ilike(f'%{value}%'))
            case _:
                return None

    def _get_default_ordering(self, query):
        return query.order_by(self.model.name)


highschool = CRUDHighSchool(Highschool)
