from typing import Annotated

from fastapi import Depends

from app.utils.unitofwork import UOW
from .service import NotificationService


def get_notification_service(uow: UOW):
    return NotificationService(uow)


NotificationServiceDep = Annotated[NotificationService, Depends(get_notification_service)]
