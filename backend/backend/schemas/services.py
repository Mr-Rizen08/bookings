from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field, field_validator, ValidationError


class ServiceBase(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    description: str | None = Field(default=None)
    duration_min: int
    price: Decimal = Field(ge=0)

    @field_validator("duration_min")
    @classmethod
    def validate_duration_min(cls, v: int | None):
        if v is None:
            return v
        if v > 0 and  v % 15 == 0:
            return v
        raise ValidationError("duration must be between 0 and 15")

class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(ServiceBase):
    name : str | None = Field(default=None, min_length=3, max_length=100)
    description : str | None = Field(default=None)
    duration_min: int | None = Field(default=None)
    price: Decimal | None  = Field(ge=0, default=None)


class ServiceBrief(BaseModel):
    id: UUID
    name: str

class ServiceRead(ServiceBase):
    id: UUID
    is_active: bool



