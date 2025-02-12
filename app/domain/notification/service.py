from app.utils.unitofwork import IUnitOfWork


class NotificationService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add(self, device_token: str):
        pass

    async def get(self, device_token: str):
        pass
