from typing import Annotated

from fastapi import Depends

from dependencies.db import SessionDep
from repository.masters import MasterRepository
from services.masters import MasterService


async def get_master_repo(
        session: SessionDep
)->MasterRepository:
    return MasterRepository(session)

MasterDep = Annotated[
    MasterRepository,
    Depends(get_master_repo)
]


async def get_master_service(
        session: SessionDep,
        master_dep: MasterDep
):
    return MasterService(session, master_dep)

MasterServiceDep = Annotated[
    MasterService,
    Depends(get_master_service)
]

