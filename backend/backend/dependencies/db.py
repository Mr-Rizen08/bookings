from typing import AsyncGenerator, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.database import SessionFactory

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionFactory() as session, session.begin():
        yield session


SessionDep = Annotated[
    AsyncSession,
    Depends(get_db),
]

#session: AsyncSession = Depends(get_db)