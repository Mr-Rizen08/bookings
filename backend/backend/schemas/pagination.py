import math
from typing import Generic, TypeVar

from fastapi import Query
from pydantic import BaseModel, Field
from pydantic import computed_field

T = TypeVar("T")

#/admin/users?page=1&size=50

class PaginationParams(BaseModel):
    page: int = Query(ge=1 ,default=1)
    size: int = Query(ge=5,le=100   ,default=5)

    @property
    def limit(self) -> int:
        return self.size

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size



class Page(
    BaseModel,
    Generic[T]
):
    items: list[T]
    total: int
    page: int = Field(ge=1 ,default=1)
    size: int = Field(ge=5,le=100 ,default=5)

    @computed_field
    @property
    def total_pages(self) -> int:
        if self.total <= 0:
            return 0
        return math.ceil(self.total / self.size)

    @computed_field
    @property
    def has_prev(self) -> bool:
        return self.page > 1


