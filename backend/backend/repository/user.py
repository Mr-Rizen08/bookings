from uuid import UUID

from sqlalchemy import select

from backend.models import User
from backend.repository.base import BaseRepository


class UserRepository(BaseRepository):
    async def create(self, user: User) -> None:
        self.session.add(user)
        await self.session.flush()

    async def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_by_id(self, user_id: UUID) -> User | None:
        stmt = select(User).where(User.id == user_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()