from datetime import datetime, timezone, timedelta

from fastapi import HTTPException
from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.secutiry import hash_password, verify_password, encode_access_token, generate_refresh_token
from models import User, RefreshToken
from repository.refresh_token import RefreshTokenRepository
from repository.user import UserRepository
from schemas.auth import RegisterUser, LoginUser


class AuthService:
    def __init__(
            self,
            session: AsyncSession,
            user_repo: UserRepository,
            refresh_token_repo: RefreshTokenRepository
    ):
        self.session = session
        self.user_repo = user_repo
        self.refresh_token_repo = refresh_token_repo

    async def register(
            self,
            body: RegisterUser
    ):
        exists_user = await self.user_repo.get_by_email(body.email)
        if exists_user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Email already registered")
        hashed_password = hash_password(body.password)

        user = User(
                email=body.email,
                full_name=body.full_name,
                phone=body.phone
        )
        await self.user_repo.create(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user


    async def login(
            self,
            body: LoginUser
    ):
        exists_user = await self.user_repo.get_by_email(body.email)
        if not  exists_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZE,
                          detail="Invalid email or password")
        hashed_password  =  verify_password(exists_user.password_hash, body.password)
        if not hashed_password:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid email or password")

        access_token = encode_access_token(exists_user.id)

        token, token_hash = generate_refresh_token()

        refresh_token = RefreshToken(
            user_id=exists_user.id,
            token_hash=token_hash,
            expires_at=datetime.now(tz=timezone.utc) + timedelta(days=30)
        )
        await self.refresh_token_repo.create(refresh_token)

        await self.session.commit()

        return exists_user
