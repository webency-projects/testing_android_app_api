from typing import Annotated

from fastapi import Depends

from app.utils.unitofwork import UOW
from .service import UserService


def get_user_service(uow: UOW):
    return UserService(uow)


UserServiceDep = Annotated[UserService, Depends(get_user_service)]
