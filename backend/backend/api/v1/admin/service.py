from uuid import UUID

from fastapi import APIRouter

from dependencies.services import ServiceServiceDep
from schemas.services import ServiceCreate, ServiceRead, ServiceUpdate

router = APIRouter(
    prefix="/services",
    tags=["services"],
)

@router.post(
    "",
    response_model=ServiceRead,
)
async def create_service(
        body: ServiceCreate,
        service: ServiceServiceDep,
):
    service = await service.create_service(body)
    return service

@router.patch("/{service_id}")
async def update_service(
        service_id: UUID,
        body: ServiceUpdate,
        service: ServiceServiceDep,
):
    await service.update_service(service_id, body)


@router.delete("/{service_id}")
async def delete_service(service_id: UUID, service: ServiceServiceDep):
    await service.delete_service(service_id)
