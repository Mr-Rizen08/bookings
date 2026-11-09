from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from backend.models import Service
from backend.repository.service import ServiceRepository
from schemas.services import ServiceCreate, ServiceUpdate


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

    async def create_service(
            self,
            body: ServiceCreate
    ):
        exist_service = await self.service_repo.get_by_name(body.name)
        if exist_service is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Service already exists"
            )
        service = Service(
            name=body.name,
            description=body.description,
            duration_min=body.duration_min,
            price=body.price
        )

        await self.service_repo.create(service)
        await self.session.commit()
        return service

    async def update_service(
            self,
            service_id: UUID,
            body: ServiceUpdate
    ) -> None:
        service = await self.service_repo.get_by_id(service_id)
        if not service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Service not found"
            )
        data = body.model_dump(exclude_none=True)

        for key, value in data.items():
            setattr(service, key, value)
        await self.session.commit()


    async def delete_service(
            self,
            service_id: UUID
    ):
        service = await self.service_repo.get_by_id(service_id)
        if not service:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Service not found"
            )
        service.is_active = False
        await self.session.commit()