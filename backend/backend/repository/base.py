from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    #Его наследники будут работать только с БД
    def __init__(self, db: AsyncSession):
        self.session = db

