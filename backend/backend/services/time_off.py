from fastapi import HTTPException
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from models import TimeOff
from repository.time_off import TimeOffRepository
from schemas.time_off import TimeOffSchema, TimeOffFilter


class TimeOffService:
    def __init__(self, session: AsyncSession, service_repo: TimeOffRepository):
        self.session = session
        self.service_repo = service_repo

    async def get_time_off_by_id(
            self,
            master_id: UUID,
            filters: TimeOffFilter
    ):
        time_offs = await self.service_repo.list_by_master(
            master_id=master_id, filters=filters)
        return time_offs


    async def remove_time_off(
            self,
            master_id: UUID,
            time_off_id: UUID
    ):
        service = await self.service_repo.get_by_id(time_off_id)
        if not service or service.master_id != master_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="TimeOff not found"
            )
        await self.service_repo.remove(master_id)
        await self.session.commit()


    async def create_time_off(
            self,
            body: TimeOffSchema,
            master_id: UUID
    ):
        time_off = TimeOff(
            master_id=master_id,
            start_time=body.start_time,
            end_time=body.end_time,
            reason=body.reason,
        )
        await self.service_repo.add_time_off(time_off)
        await self.session.commit()
        return time_off


