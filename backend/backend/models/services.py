from decimal import Decimal
from sqlalchemy import String, CheckConstraint, NUMERIC, Boolean, Table, ForeignKey, Column, Uuid
from sqlalchemy.orm import Mapped, mapped_column
from backend.models.base import Base
from backend.models.mixins import IdMixin


class Service(IdMixin, Base):
    __tablename__ = "services"
    __table_args__ = (
        CheckConstraint( "duration_min > 0 AND duration_min % 15 = 0",name="ck_duration_min"),
        CheckConstraint("price >= 0", name="ck_price")
    )

    name : Mapped[str] = mapped_column(String(100), unique=True,nullable=False)
    description : Mapped[str | None]
    duration_min: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[Decimal] = mapped_column(NUMERIC(12, 2), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


master_service = Table(
    "master_services",
    Base.metadata,
    Column("master_id", Uuid, ForeignKey("services.id"), primary_key=True),
    Column("service_id", Uuid, ForeignKey("services.id"), primary_key=True),
)

