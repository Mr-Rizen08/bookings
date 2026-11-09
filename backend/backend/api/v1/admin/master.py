from uuid import UUID

from fastapi import APIRouter

from dependencies.masters import MasterServiceDep
from schemas.masters import MasterCreate, MasterRead, MasterServiceUpdate

router = APIRouter(
    prefix="/master",
    tags=["master"],
)

@router.post(
    "",
    response_model=MasterRead,
)
async def create_service(
        body: MasterCreate,
        service: MasterServiceDep
):
    master = await service.create_master(body)
    return master


@router.patch(
    "/{master_id}/services"
)
async def update_master_services(
        master_id: UUID,
        body: MasterServiceUpdate,
        service: MasterServiceDep
):
    await service.change_services(master_id, body)

@router.patch("/{master_id}")
async def update_master(
        master_id: UUID,
):
    ...

