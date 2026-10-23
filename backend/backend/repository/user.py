from sqlalchemy import select

from models import User
from repository.base import BaseRepository


class UserRepository(BaseRepository):
    async def create(self, user: User) -> None:
        self.session.add(user)
        await self.session.flush()

    async def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
