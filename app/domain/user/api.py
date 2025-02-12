from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus
from .deps import UserServiceDep
from .schema import UserRequest

user_api = APIRouter(prefix="/user")


@user_api.post
async def create(user: UserRequest, user_service: UserServiceDep):
    response = await user_service.create(user)
    return JSONResponse(content=response, status_code=HTTPStatus.CREATED)


@user_api.get("/{user_id}")
async def get(user_id: int, user_service: UserServiceDep):
    response = await user_service.get(user_id)
    return JSONResponse(content=response, status_code=HTTPStatus.OK)


@user_api.get
async def get_all(user_service: UserServiceDep):
    response = await user_service.get_all()
    return JSONResponse(content=response, status_code=HTTPStatus.OK)
