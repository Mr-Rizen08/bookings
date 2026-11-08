from fastapi import APIRouter

from backend.dependencies.auth import CurrentUserDep
from backend.schemas.users import UserRead
from dependencies.user import UserServiceDep
from schemas.users import UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["users"],
)
@router.get(
    "/me",
    response_model=UserRead,
)
async def get_me(
        user: CurrentUserDep
):
    return user

@router.patch(
    "/me",

)
async def update_me(
        user: CurrentUserDep,
        body: UserUpdate,
        service: UserServiceDep
):
    await service.update(
        user_id=user.id,
        body=body
    )
