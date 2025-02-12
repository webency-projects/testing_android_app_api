from typing import AsyncGenerator
from sqlalchemy import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from .config import settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,
    future=True,
    pool_size=75,
    max_overflow=125,
    pool_recycle=600,
    pool_pre_ping=True,
    poolclass=AsyncAdaptedQueuePool
)

async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
