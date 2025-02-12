from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from model import Account
from typing import List


class UserRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self, limit: int) -> List[Account]:
        stmt = select(Account).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars() or []

    async def get_one(self, user_id: int) -> Account | None:
        stmt = select(Account).where(Account.id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Account | None:
        stmt = select(Account).where(Account.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(self, email: str, password: str) -> Account:
        user = await self.get_by_email(email)
        if not user:
            user = Account(email=email, password=password)
            self.session.add(user)
        return user
