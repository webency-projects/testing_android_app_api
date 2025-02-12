from abc import ABC, abstractmethod
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session_maker
from app.domain.device.repository import DeviceRepository
from app.domain.notification.repository import NotificationRepository
from app.domain.user.repository import UserRepository


class IUnitOfWork(ABC):
    session: AsyncSession
    user: UserRepository
    device: DeviceRepository
    notification: NotificationRepository

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.user = UserRepository(self.session)
        self.device = DeviceRepository(self.session)
        self.notification = NotificationRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def rollback(self):
        await self.session.rollback()

    async def commit(self):
        await self.session.commit()


UOW = Annotated[IUnitOfWork, Depends(UnitOfWork)]
