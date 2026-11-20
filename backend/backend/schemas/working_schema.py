from datetime import time
from pydantic import BaseModel
from models.working_hours import WeekdayEnum


class WorkingHourSchema(BaseModel):
    weekday: WeekdayEnum
    start_time: time
    end_time: time



class WorkingHoursSchema(BaseModel):
    items: list[WorkingHourSchema]
