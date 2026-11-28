from pydantic import BaseModel
from datetime import time

class TimeOffSchema(BaseModel):
    start_time: time
    end_time: time
    reason: str | None

class ListTimeOffSchema(BaseModel):
    items: list[TimeOffSchema]
