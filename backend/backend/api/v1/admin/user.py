from uuid import UUID

from fastapi import APIRouter, Depends

from dependencies.user import UserServiceDep
from schemas.pagination import PaginationParams, Page
from schemas.users import UserRead, UserFilter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.get(
    "",
    response_model=Page[UserRead])
async def get_users(
        service: UserServiceDep,
        filters: UserFilter = Depends(),
        pagination: PaginationParams = Depends(),
):
    response = await service.list_paginated(filters, pagination)
    return response

@router.post(
    "/{user_id}/active"
)
async def activate_user(user_id: UUID):
    pass

@router.post(
    "/{user_id}/deactive"
)
async def deactivate_user(user_id: UUID):
    pass


@router.get("/{user_id}")
async def get_user(user_id: UUID):
    pass
