from uuid import UUID

from fastapi import APIRouter
from starlette import status
from backend.dependencies.services import ServiceServiceDep
from backend.schemas.services import ServiceRead

router = APIRouter(
    prefix="/services",
    tags=["services"],
)

@router.get(
    "",
    summary="Получение всех Услуг",
    response_model=list[ServiceRead],
    status_code=status.HTTP_200_OK,
)
async def get_services(
        session: ServiceServiceDep
):
    response = await session.get_services()
    return response




@router.get(
    "{/service_id}",
    summary="Получение Дететальной иформации услуги",
    response_model=ServiceRead,
    status_code=status.HTTP_200_OK
)
async def get_service(
        service_id: UUID,
        service: ServiceServiceDep
):
    response = await service.get_service_by_id(service_id)
    return response



