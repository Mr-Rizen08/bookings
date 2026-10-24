from typing import Annotated

from fastapi import Depends

from backend.dependencies.db import SessionDep
from backend.repository.user import UserRepository


async def get_user_repo(
        session: SessionDep
) -> UserRepository:
    return UserRepository(session)

UserRepoDep = Annotated[
    UserRepository,
    Depends(get_user_repo)
]

