from models import RefreshToken
from repository.base import BaseRepository


class RefreshTokenRepository(BaseRepository):
    async def create(self, refresh_token: RefreshToken) -> None:
        self.session.add(refresh_token)
        await self.session.flush()

