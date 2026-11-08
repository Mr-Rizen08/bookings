from enum import Enum
from uuid import UUID
import phonenumbers as pn
from fastapi import Query
from phonenumbers.phonenumberutil import NumberParseException
from pydantic import BaseModel, Field, field_validator
from sqlalchemy import Select, or_
from models.user import UserRoleEnum, User
from schemas.filters import BaseFilter


class UserUpdate(BaseModel):
    fullname: str | None = Field(default=None, max_length=320)
    phone: str | None = Field(default=None, max_length=20)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str | None):
        if v is None:
            return None
        try:
            parsed = pn.parse(v, None)
        except NumberParseException:
            pass
        if any(c.isalpha() for c in v):
            raise ValueError("Invalid number")
        return v

class UserRead(BaseModel):
    id: UUID
    email: str
    full_name: str
    phone: str
    role: UserRoleEnum
    is_active: bool

class UserSortEnum(str, Enum):
    full_name_asc = "full_name:asc"
    full_name_desc = "full_name:desc"
    role_asc = "role:asc"
    role_desc = "role:desc"

class UserFilter(BaseFilter, BaseModel):
    q: str | None = Query(default=None)
    role: UserRoleEnum | None = Query(default=None)
    sort_by:UserSortEnum = Query(alias="sort", default=UserSortEnum.full_name_asc)

    def filter(
            self,
            stmt: Select
    ) -> Select:
        if self.role is not None:
            stmt = stmt.where(User.role == self.role)
        if self.q is not None:
            pattern = f"%{self.q}%"
            stmt = stmt.where(
                or_(
                    User.full_name.ilike(pattern),
                    User.email.ilike(pattern)
                )
            )
        return stmt

    def sort(
            self,
            stmt: Select
    ) -> Select:
        _MAP_COLUMNS = {
            UserSortEnum.full_name_asc: User.full_name.asc(),
            UserSortEnum.full_name_desc: User.full_name.desc(),
            UserSortEnum.role_asc: User.role.asc(),
            UserSortEnum.role_desc: User.role.desc()
        }
        column = _MAP_COLUMNS.get(self.sort_by)
        if column is None:
            return stmt
        stmt = stmt.order_by(column)
        return stmt