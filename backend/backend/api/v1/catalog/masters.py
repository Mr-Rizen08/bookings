from uuid import UUID

from fastapi import APIRouter
from starlette import status
from backend.dependencies.masters import MasterServiceDep
from backend.schemas.masters import MasterRead

router = APIRouter(
    prefix="/masters",
    tags=["masters"],
)


@router.get(
    "",
    summary="Get all masters",
    response_model=list[MasterRead],
    status_code=status.HTTP_200_OK,
)
async def get_masters(
        session: MasterServiceDep
):
    response = await session.get_masters()
    return response


@router.get(
    "/{master_id}/slots",
    summary="Get a master's slots",
    status_code=status.HTTP_200_OK,
)
async def get_slots(master_id: UUID):
    pass





@router.get(
    "/{master_id}",
    summary="Get a master",
    response_model=MasterRead,
    status_code=status.HTTP_200_OK,
)
async def get_master(
        master_id: UUID,
        session: MasterServiceDep
):
    response = await session.get_master_by_id(master_id)
    return response


