from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from contextlib import asynccontextmanager
from src.core.config import settings

engine = create_async_engine(settings.get_database_url, echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


@asynccontextmanager
async def get_session():
    async with async_session_maker as session:
        yield session
