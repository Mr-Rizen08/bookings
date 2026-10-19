from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from models import Service
from repository.service import ServiceRepository


class ServiceService:
    def __init__(
            self,
            session: AsyncSession,
            service_repo: ServiceRepository,
    ) -> None:
        self.session = session
        self.service_repo = service_repo



    async def get_service_by_id(
            self,
            service_id: UUID
    ) -> Service:
        service = await self.service_repo.get_by_id(service_id)
        if not service:
            raise HTTPException(
                status_code=404,
                detail="Service not found"
            )
        return service

    async def get_services(
            self
    )-> list[Service]:
        services = await self.service_repo.list()
        return services
