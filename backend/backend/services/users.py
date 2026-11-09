from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from repository.user import UserRepository
from schemas.pagination import PaginationParams
from schemas.users import UserUpdate, UserFilter


class UserService:
    def __init__(
            self,
            session: AsyncSession,
            user_repo: UserRepository,
    ):
        self.session = session
        self.user_repo = user_repo

    async def update(
            self,
            user_id: UUID,
            body: UserUpdate,
    )-> None:
        user = await self.user_repo.get_by_id(user_id, True)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not user.is_active:
            raise HTTPException(status_code=404, detail="User account is disabled")

        data = body.model_dump(exclude_none=True)

        for key, value in data.items():
            setattr(user, key, value)

        await self.session.commit()

    async def get_by_id(self,
                        user_id: UUID
    ) -> User:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def list_paginated(
            self,
            filters: UserFilter,
            pagination: PaginationParams
    ):
        users = await self.user_repo.list_paginated(filters, pagination)
        return users

    async def activate(self, user_id: UUID) -> None:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.is_active = True

        await self.session.commit()


    async def deactivate(self, user_id: UUID) -> None:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.is_active = False

        await self.session.commit()
