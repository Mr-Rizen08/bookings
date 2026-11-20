from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from repository.working_hours import WorkingHoursRepository
from schemas.working_schema import WorkingHoursSchema


class WorkingHoursService:
    def __init__(self, session: AsyncSession, working_hours_repo: WorkingHoursRepository):
        self.session = session
        self.working_hours_repo = working_hours_repo

    async def get_master_working_hours(self,
                                       master_id: UUID
                                       ):
        workings_hours = await self.working_hours_repo.get_by_master(master_id)
        return workings_hours

    async def update_working_hours(
            self,
            master_id: UUID,
            working_hours: WorkingHoursSchema
    ):
        await self.working_hours_repo.save_all(master_id=master_id, items=working_hours.items)
        await self.session.commit()