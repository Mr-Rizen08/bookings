from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from backend.models import Base
from backend.models.mixins import IdMixin


class RefreshToken(IdMixin, Base):
    __tablename__ = 'refresh_token'

    user_id : Mapped[UUID] = mapped_column(ForeignKey("user.id", ondelete='CASCADE'), index=True)
    token_hash: Mapped[str] = mapped_column(String(64))
    expires_at: Mapped[datetime]
    revoked_at: Mapped[datetime]

    user: Mapped["User"] = relationship(back_populates="refresh_token")