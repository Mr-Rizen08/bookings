from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post(
    "/login",
    summary="Вход в уч запись",
    status_code=status.HTTP_201_CREATED,
)
async def register():
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

