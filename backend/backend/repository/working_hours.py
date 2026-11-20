from uuid import UUID
from sqlalchemy import delete, select, insert
from models import WorkingHours
from repository.base import BaseRepository
from schemas.working_schema import WorkingHourSchema


class WorkingHoursRepository(BaseRepository):
    async def save_all(
            self,
            master_id: UUID,
            items: list[WorkingHourSchema]
    ):
        delete_stmt = delete(WorkingHours).where(
            WorkingHours.master_id == master_id
        )
        await self.session.execute(delete_stmt)

        await self.session.execute(
            insert(WorkingHours),
            [
                {
                    "master_id": master_id,
                    "weekend": item.weekday,
                    "start_time": item.start_time,
                    "end_time": item.end_time,
                }
                for item in items
            ]
        )
        await self.session.flush()

    async def get_by_master(
            self,
            master_id: UUID) -> list[WorkingHours]:
        stmt = select(WorkingHours).where(
            WorkingHours.master_id == master_id
        )
        results = await self.session.execute(stmt)

        return list(results.scalars().all())