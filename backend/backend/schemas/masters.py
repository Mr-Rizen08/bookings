from uuid import UUID

from pydantic import BaseModel

from schemas.services import ServiceBrief


class MasterRead(BaseModel):
    id: UUID
    display_name: str
    bio: str
    is_active: bool
    services: list[ServiceBrief]

