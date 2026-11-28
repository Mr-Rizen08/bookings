from uuid import UUID

from sqlalchemy import select

from models import TimeOff
from repository.base import BaseRepository


class TimeOffRepository(
    BaseRepository
):
    async def add_time_off(self, time_off: TimeOff):
        self.session.add(time_off)
        await self.session.flush()

    async def list(self):
        pass

    async def remove(self, time_off_id: UUID):
        await self.session.delete(time_off_id)
        await self.session.flush()

    async def get_by_id(self, time_off_id: UUID) -> TimeOff | None:
        stmt = select(TimeOff).where(TimeOff.id == time_off_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()