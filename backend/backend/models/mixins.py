from uuid import uuid4

from asyncpg.pgproto.pgproto import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column


class IdMixin:
    id : Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)