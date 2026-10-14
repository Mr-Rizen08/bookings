from datetime import datetime
from enum import Enum
from uuid import UUID

from sqlalchemy import ForeignKey, SMALLINT, CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.models import Base
from backend.models.mixins import IdMixin

class WeekdayEnum(int,Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

class WorkingHours(IdMixin, Base):
    __tablename__ = "working_hours"
    __table_args__ = (
        CheckConstraint("weekday BETWEEN 1 AND 7", name="ck_weekday"),
        CheckConstraint("ends_at > starts_at", name="ck_ends_at"),
    )
    master_id: Mapped[UUID] = mapped_column(ForeignKey("master.id", ondelete="CASCADE"),nullable=False)
    weekday: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    starts_at: Mapped[datetime] = mapped_column(nullable=False)
    ends_at: Mapped[datetime] = mapped_column(nullable=False)


class TimeOff(IdMixin, Base):
    __tablename__ = "time_off"
    __table_args__ = (
        CheckConstraint("ends_at > starts_at", name="ck_ends_at"),
    )
    master_id: Mapped[UUID] = mapped_column(ForeignKey("master.id", ondelete="CASCADE"), nullable=False)
    starts_at: Mapped[datetime] = mapped_column(nullable=False)
    ends_at: Mapped[datetime] = mapped_column(nullable=False)
    reason : Mapped[str] = mapped_column(String(200), nullable=True)

