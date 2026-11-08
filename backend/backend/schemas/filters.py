from abc import ABC, abstractclassmethod, abstractmethod

from sqlalchemy import Select


class BaseFilter(ABC):
    @abstractmethod
    def filter(
            self,
            stmt: Select
    ) -> Select:
        pass

    @abstractmethod
    def sort(
            self,
            stmt: Select
    ) -> Select:
        pass
