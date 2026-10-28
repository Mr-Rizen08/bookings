from typing import Annotated
from fastapi import Depends, HTTPException
from starlette import status

from backend.dependencies.db import SessionDep
from backend.dependencies.user import UserRepoDep
from backend.repository.refresh_token import RefreshTokenRepository
from backend.services.auth import AuthService
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from core.secutiry import  decode_access_token
from models import User

oauth2_bearer = HTTPBearer()

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

#Header: Authorization: Bearder Token
async def get_current_user(
          credentials: Annotated[
              HTTPAuthorizationCredentials,
              Depends(oauth2_bearer)
          ],
        user_repo: UserRepoDep,
) -> User:
    token = credentials.credentials
    user_id = decode_access_token(token)
    user = await user_repo.get_by_id(user_id)
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
        )
    return user

CurrentUserDep = Annotated[
    User,
    Depends(get_current_user)
]