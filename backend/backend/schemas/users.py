from uuid import UUID

from pydantic import BaseModel

from models.user import UserRoleEnum


class UsersRead(BaseModel):
    id: UUID
    email: str
    full_name: str
    phone: str
    role: UserRoleEnum
    is_active: bool


