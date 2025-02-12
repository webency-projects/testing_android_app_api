from sqlalchemy.ext.asyncio import AsyncSession


class DeviceRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

