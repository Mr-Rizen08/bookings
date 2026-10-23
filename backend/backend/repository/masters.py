from uuid import UUID

from sqlalchemy import select

from models import Master
from repository.base import BaseRepository


class MasterRepository(BaseRepository):
    async def create(self, master: Master) -> None:
        self.session.add(master)
        await self.session.flush()

    async def get_by_id(self, master_id: UUID) -> Master | None:
        stmt = select(Master).where(Master.id == master_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def list(self):
        stmt = select(Master)
        result = await self.session.execute(stmt)
        return result.scalars().all()
