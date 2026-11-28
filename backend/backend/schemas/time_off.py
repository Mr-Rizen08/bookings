from uuid import UUID

from fastapi import Query
from pydantic import BaseModel
from datetime import datetime

class TimeOffFilter(BaseModel):
    from_at: datetime | None = Query(default=None, alias="from")
    to_at: datetime | None = Query(default=None, alias="to")

class TimeOffSchema(BaseModel):
    start_time: datetime
    end_time: datetime
    reason: str | None

class TimeOffRead(TimeOffSchema):
    id: UUID

