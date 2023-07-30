from app.models.highschool import Highschool
from app.schemas.highschool import GettingHighSchool
from .universal import transform


def get_high_school(high_school: Highschool) -> GettingHighSchool:
    return transform(
        high_school,
        GettingHighSchool
    )