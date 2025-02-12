from app.utils.unitofwork import IUnitOfWork
from app.utils.token import generate_hash_token


class DeviceService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def add_device(self):
        pass


