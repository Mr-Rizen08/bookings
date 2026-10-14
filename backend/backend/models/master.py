from uuid import UUID

from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationships, relationship

from backend.models.base import Base
from backend.models.mixins import IdMixin


class Master(IdMixin, Base):
    __tablename__ = "masters"

    user_id : Mapped[UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    display_name : Mapped[str] = mapped_column(String(100), nullable=False)
    bio : Mapped[str] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # user: Mapped["User"] = relationship(backref="")
