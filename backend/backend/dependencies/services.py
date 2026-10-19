from typing import Annotated
from fastapi import Depends
from dependencies.db import SessionDep
from repository.service import ServiceRepository
from services.service import ServiceService


#Session -> ServiceRepository

#get_db -> AsyncSession
#AsyncSession -> ServiceRepository

async def get_service_repo(
        session: SessionDep
) -> ServiceRepository:
    return ServiceRepository(session)


ServiceRepoDep = Annotated[
    ServiceRepository,
    Depends(get_service_repo)
]



async def get_service_service(
        session: SessionDep,
        service_repo: ServiceRepoDep
):
    return ServiceService(session, service_repo)

ServiceServiceDep = Annotated[
    ServiceService,
    Depends(get_service_service)
]

