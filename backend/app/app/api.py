from fastapi import APIRouter

from app.endpoints import login, users, email_verification_code, highschool, highschool_request

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(email_verification_code.router)
api_router.include_router(highschool.router)
api_router.include_router(highschool_request.router)

