from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from backend.models import Master
from backend.repository.masters import MasterRepository
from core.secutiry import generate_strong_password, hash_password
from models.user import UserRoleEnum, User
from repository.service import ServiceRepository
from repository.user import UserRepository
from schemas.masters import MasterCreate, MasterServiceUpdate


class MasterService:
    def __init__(
            self,
            session: AsyncSession,
            master_repo: MasterRepository,
            user_repo: UserRepository,
            service_repo: ServiceRepository
    )->None:
        self.session: AsyncSession = session
        self.master_repo: MasterRepository = master_repo
        self.user_repo = user_repo
        self.service_repo = service_repo

    async def create_master(
            self,
            body: MasterCreate,
    ) -> Master:
        exist_user = await self.user_repo.get_by_email(body.email)
        if exist_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already exists"
            )

        password  = generate_strong_password()
        hashed_password = hash_password(password)

        user = User(
            email=body.email,
            full_name=body.full_name,
            role=UserRoleEnum.master,
            phone=body.phone,
            password_hash=hashed_password
        )

        await self.user_repo.create(user)

        master = Master(
            user_id=user.id,
            bio=body.bio,
            display_name=user.full_name,
        )

        await self.master_repo.create(master)
        await self.session.commit()

        # отправка по почте


        return master

    async def  get_master_by_id(
            self,
            master_id: UUID)->Master:
        master = await self.master_repo.get_by_id(master_id)
        if not master:
            raise HTTPException(
                status_code=404,
                detail="Master not found")
        return master


    async def change_services(
            self,
            master_id: UUID,
            body: MasterServiceUpdate
    ):
        master = await self.master_repo.get_by_id(master_id)

        if not master:
            raise HTTPException(
                status_code=404,
                detail="Master not found"
            )

        services = await self.service_repo.list_by_ids(body.service_ids)

        master.services = services

        await self.session.commit()


    async def get_masters(
            self,
    )->list[Master]:
        masters = await self.master_repo.list()
        return masters

