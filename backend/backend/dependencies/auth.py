from typing import Annotated
from fastapi import Depends
from backend.dependencies.db import SessionDep
from backend.dependencies.user import UserRepoDep
from backend.repository.refresh_token import RefreshTokenRepository
from backend.services.auth import AuthService


async def get_refresh_repo(
        session: SessionDep,
) -> RefreshTokenRepository:
    return RefreshTokenRepository(session)

RefreshRepoDep = Annotated[
    RefreshTokenRepository,
    Depends(get_refresh_repo),
]

async def get_auth_services(
        session: SessionDep,
        user_repo: UserRepoDep,
        refresh_repo: RefreshRepoDep,
) -> AuthService:
    return AuthService(
        session=session,
        user_repo=user_repo,
        refresh_token_repo=refresh_repo,
    )

AuthServiceDep = Annotated[
    AuthService,
    Depends(get_auth_services)
]