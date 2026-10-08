from enum import Enum

from datetime import datetime

from sqlalchemy import String, BigInteger, Boolean, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base
from backend.models.mixins import IdMixin


class UserRoleEnum(str, Enum):
    client = 'client'
    admin = 'admin'
    master = 'master'

class User(IdMixin ,Base):
    __tablename__ = 'user'

    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(320), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    role: Mapped[str] = mapped_column(String(20), default=UserRoleEnum.client)
    telegram_chad_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now, server_onupdate=func.now)



