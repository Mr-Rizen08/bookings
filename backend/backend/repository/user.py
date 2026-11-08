from uuid import UUID

from sqlalchemy import select, func

from backend.models import User
from backend.repository.base import BaseRepository
from schemas.pagination import PaginationParams, Page
from schemas.users import UserFilter


class UserRepository(BaseRepository):
    async def create(self, user: User) -> None:
        self.session.add(user)
        await self.session.flush()

    async def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_id(self, user_id: UUID , for_update: bool = False) -> User | None:
        stmt = select(User).where(User.id == user_id)
        if for_update:
            stmt = stmt.with_for_update() # USER
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def list_paginated(
            self,
            filters: UserFilter,
            pagination: PaginationParams
    ):
        stmt = select(User)
        stmt = filters.filter(stmt)
        stmt = filters.sort(stmt)

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total = (await self.session.execute(count_stmt)).scalar_one()

        stmt = stmt.offset(pagination.offset).limit(pagination.limit)

        result = await self.session.execute(stmt)
        users = result.scalars().all()

        return Page(
            total=total,
            page=pagination.page,
            items=list(users),
            size=pagination.size
        )