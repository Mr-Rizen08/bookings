from typing import Annotated

from fastapi import Depends

from backend.dependencies.db import SessionDep
from backend.repository.masters import MasterRepository
from backend.services.masters import MasterService


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

