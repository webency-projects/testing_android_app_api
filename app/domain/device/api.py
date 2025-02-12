from fastapi.routing import APIRouter
from .deps import DeviceServiceDep
device_api = APIRouter(prefix="/device")


async def add(device_service: DeviceServiceDep):
    pass


async def delete(device_service: DeviceServiceDep):
    pass
