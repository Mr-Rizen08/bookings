from datetime import datetime
from enum import Enum
from uuid import UUID

from sqlalchemy import ForeignKey, CheckConstraint, NUMERIC, String, func
from sqlalchemy.orm import mapped_column, Mapped

from backend.models import Base
from backend.models.mixins import IdMixin

class StatusEnum(str, Enum):
    ...


class Booking(IdMixin, Base):
    __tablename__ = 'booking'
    __table_args__ = (
        CheckConstraint("ends_at > starts_at", name="ck_ends_at"),
    )
    client_id : Mapped[UUID] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    master_id: Mapped[UUID] = mapped_column(ForeignKey("master.id", ondelete="CASCADE"), nullable=False)
    service_id: Mapped[UUID] = mapped_column(ForeignKey("service.id", ondelete="CASCADE"), nullable=False)
    starts_at: Mapped[datetime] = mapped_column(nullable=False)
    ends_at: Mapped[datetime] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False, default="pending")
    price: Mapped[float] = mapped_column(NUMERIC(12,2), nullable=False)
    duration_min: Mapped[int] = mapped_column(nullable=False)
    idempotency_key: Mapped[UUID] = mapped_column(nullable=True)
    expires_at: Mapped[datetime] = mapped_column(nullable=True)
    cancelled_at: Mapped[datetime] = mapped_column(nullable=True)
    cancel_reason: Mapped[str] = mapped_column(String(200), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(nullable=False, default=func.now())