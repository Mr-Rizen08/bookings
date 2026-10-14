from uuid import UUID

from fastapi import APIRouter
from starlette import status

from models import Master
from schemas.masters import MasterRead

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
async def get_masters():
    ...




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
async def get_master(master_id: UUID):
    ...

