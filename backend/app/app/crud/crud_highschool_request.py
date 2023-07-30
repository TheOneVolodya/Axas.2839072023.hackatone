from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union

from sqlalchemy import desc, orm
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.highschool import Highschool
from app.models.highschool_request import HighschoolRequest
from app.schemas.base import BaseSchema
from app.schemas.highschool_request import CreatingHighschoolRequest, UpdatingHighschoolRequest
from app.schemas.highschool import CreatingHighSchool, UpdatingHighSchool
from app.utils.code import fake_gen


class CRUDHighSchoolRequest(CRUDBase[HighschoolRequest, CreatingHighschoolRequest, UpdatingHighschoolRequest]):

    def _get_default_ordering(self, query):
        return query.order_by(self.model.created)


highschool_request = CRUDHighSchoolRequest(HighschoolRequest)
