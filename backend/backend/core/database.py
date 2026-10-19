from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.configs import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True
)

SessionFactory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)