from uuid import UUID
import phonenumbers as pn
from phonenumbers import NumberParseException
from pydantic import BaseModel, EmailStr, Field, field_validator
from backend.schemas.services import ServiceBrief

class MasterCreate(BaseModel):
    email: EmailStr
    full_name: str = Field(max_length=100)
    phone: str | None = Field(default=None, max_length=20)
    bio: str

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str | None):
        if v is None:
            return None
        try:
            pn.parse(v, None)
        except NumberParseException:
            pass
        if any(c.isalpha() for c in v):
            raise ValueError("Invalid number")
        return v

class MasterServiceUpdate(BaseModel):
    service_ids: list[UUID]


class MasterRead(BaseModel):
    id: UUID
    display_name: str
    bio: str
    is_active: bool
    services: list[ServiceBrief]

