from uuid import UUID

from sqlalchemy import select

from models import Service
from repository.base import BaseRepository


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

    async def list(self):
        stmt = select(Service)
        result = await self.session.execute(stmt)
        return result.scalars().all()

