class EntityError(ValueError):

    http_status = 400

    def __init__(self, message=None, description=None, num=0, path=None):
        self.message = message
        self.num = num
        self.description = description or message
        self.path = path


class UnfoundEntity(EntityError):
    http_status = 404


class InaccessibleEntity(EntityError):
    http_status = 403


class UnprocessableEntity(EntityError):
    http_status = 422


class ListOfEntityError(ValueError):
    def __init__(self, errors: list[EntityError], description: str, http_status: int):
        self.errors = errors
        self.description = description
        self.http_status = http_status
