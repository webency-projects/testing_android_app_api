from typing import Annotated

from fastapi import Depends

from app.utils.unitofwork import UOW
from .service import DeviceService


def get_device_service(uow: UOW):
    return DeviceService(uow)


DeviceServiceDep = Annotated[DeviceService, Depends(get_device_service)]
