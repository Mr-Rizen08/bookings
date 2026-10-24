from enum import Enum

from datetime import datetime

from sqlalchemy import String, BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base
from backend.models.mixins import IdMixin


class UserRoleEnum(str, Enum):
    client = 'client'
    admin = 'admin'
    master = 'master'

class User(IdMixin ,Base):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(320), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    role: Mapped[str] = mapped_column(String(20), default=UserRoleEnum.client)
    telegram_chat_id: Mapped[int | None] = mapped_column(BigInteger, unique=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())



