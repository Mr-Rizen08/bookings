from uuid import UUID

from fastapi import APIRouter
from starlette import status

from models import Service
from schemas.services import ServiceRead

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
async def get_services():
    ...


@router.get(
    "{/service_id}",
    summary="Получение Дететальной иформации услуги",
    response_model=ServiceRead,
    status_code=status.HTTP_200_OK
)
async def get_service(service_id: UUID):
    ...


