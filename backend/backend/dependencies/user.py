from typing import Annotated

from fastapi import Depends

from backend.dependencies.db import SessionDep
from backend.repository.user import UserRepository
from services.users import UserService


async def get_user_repo(
        session: SessionDep
) -> UserRepository:
    return UserRepository(session)

UserRepoDep = Annotated[
    UserRepository,
    Depends(get_user_repo)
]

async def get_user_service(
        session: SessionDep,
        user_repo: UserRepoDep
) -> UserService:
    return UserService(
        session=session,
        user_repo=user_repo
    )

UserServiceDep = Annotated[
    UserService,
    Depends(get_user_service)
]
