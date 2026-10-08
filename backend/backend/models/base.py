from datetime import timezone, datetime
from sqlalchemy import TypeDecorator, DateTime
from sqlalchemy.orm import DeclarativeBase

class UTCDateTime(TypeDecorator):
    impl = DateTime(timezone=True)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        if value.tzinfo is None:
            raise ValueError("naive datetime не допускается")
        return value.astimezone(timezone.utc)

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        if value.tzinfo is None:  # SQLite/MySQL возвращают naive
            return value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc)



class Base(DeclarativeBase):
    type_annotation_map={datetime: UTCDateTime}


