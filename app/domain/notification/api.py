from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus
from .deps import NotificationServiceDep
notification_api = APIRouter(prefix="/notification")


@notification_api.post("/{device_token}")
async def add(device_token: str, notification_service: NotificationServiceDep):
    response = await notification_service.add(device_token)
    return JSONResponse(content=response, status_code=HTTPStatus.OK)


@notification_api.get("/{device_token}")
async def get(device_token: str, notification_service: NotificationServiceDep):
    response = await notification_service.get(device_token)
    return JSONResponse(content=response, status_code=HTTPStatus.OK)




