from sqlalchemy import select
from backend.models import RefreshToken
from backend.repository.base import BaseRepository


class RefreshTokenRepository(BaseRepository):
    async def create(self, refresh_token: RefreshToken) -> None:
        self.session.add(refresh_token)
        await self.session.flush()

    async def get_by_token(self, token_hash: str) -> RefreshToken | None :
        stmt = select(RefreshToken).where(RefreshToken.token_hash == token_hash)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()