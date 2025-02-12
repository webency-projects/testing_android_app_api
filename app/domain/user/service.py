from app.utils.unitofwork import IUnitOfWork


class UserService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def get_all(self):
        async with self.uow:
            result = await self.uow.user.get_all(50)
            return result

    async def get(self, account_id: int):
        async with self.uow:
            result = await self.uow.user.get_one(account_id)
            return result

    async def create(self, email: str, password: str):
        result = await self.uow.user.create(email, password)
        return result
