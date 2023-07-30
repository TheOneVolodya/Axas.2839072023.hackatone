from app.models import HighschoolRequest
from app.schemas import GettingHighschoolRequest
from app.getters import get_high_school, transform

def get_highschool_request(high_school_request: HighschoolRequest) -> GettingHighschoolRequest:
    return transform(
        high_school_request,
        GettingHighschoolRequest,
        highschool=get_high_school(high_school_request.high_school)
            if high_school_request.high_school is not None
            else None
    )