from uuid import UUID

from sqlalchemy import select

from backend.models import Service
from backend.repository.base import BaseRepository


class ServiceRepository(BaseRepository):
    async def create(self, service: Service) -> None:
        self.session.add(service)
        await self.session.flush()

    async def get_by_id(
            self,
            service_id: UUID) -> Service | None:
            stmt = select(Service).where(Service.id == service_id)
            result = await self.session.execute(stmt)
            return result.scalar_one_or_none()

    async def get_by_name(
            self,
            service_name: str
    ) -> Service | None:
        stmt = select(Service).where(Service.name == service_name)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def list(self):
        stmt = select(Service)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def list_by_ids(
            self,
            service_ids):
        stmt = select(Service).where(Service.id.in_(service_ids))
        result = await self.session.execute(stmt)
        return result.scalars().all()

