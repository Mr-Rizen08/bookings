from fastapi import APIRouter
from starlette import status

from schemas.auth import RegisterUser

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post(
    "/login",
    summary="Вход в уч запись",
    status_code=status.HTTP_201_CREATED,
)
async def register(
        body: RegisterUser
):
    pass

@router.post(
    "/register",
    summary="Регистрация",
    status_code=status.HTTP_201_CREATED,
)
async def register(
        body: RegisterUser
):
    pass


@router.post(
    "/logout",
    summary="Выход из уч",
    status_code=status.HTTP_204_NO_CONTENT
)
async def logout():
    ...


@router.post(
    "/refresh",
    summary="Обновление токенов",
    status_code=status.HTTP_201_CREATED,
)
async def refresh(): ...

