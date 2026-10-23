from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from models import Master
from repository.masters import MasterRepository

class MasterService:
    def __init__(
            self,
            session: AsyncSession,
            master_repo: MasterRepository,
    )->None:
        self.session: AsyncSession = session
        self.master_repo: MasterRepository = master_repo

    async def  get_master_by_id(
            self,
            master_id: UUID)->Master:
        master = await self.master_repo.get_by_id(master_id)
        if not master:
            raise HTTPException(
                status_code=404,
                detail="Master not found")
        return master


    async def get_masters(
            self,
    )->list[Master]:
        masters = await self.master_repo.list()
        return masters

