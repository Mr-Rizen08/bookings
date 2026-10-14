from uuid import uuid4, UUID
from sqlalchemy.orm import Mapped, mapped_column

class IdMixin:
    id : Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)