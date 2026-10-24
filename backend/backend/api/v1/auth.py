from fastapi import APIRouter
from starlette import status

from backend.dependencies.auth import AuthServiceDep
from backend.schemas.auth import RegisterUser, LoginUser, TokenResponse, TokenSchema

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post(
    "/login",
    summary="Вход в уч запись",
    status_code=status.HTTP_201_CREATED,
    response_model=TokenResponse,
)
async def login(
        body: LoginUser,
        service: AuthServiceDep
):
    response = await service.login(body)
    return response

@router.post(
    "/register",
    summary="Регистрация",
    status_code=status.HTTP_201_CREATED,
)
async def register(
        body: RegisterUser,
        service: AuthServiceDep
):
    response = await service.register(body)
    return response

@router.post(
    "/logout",
    summary="Выход из уч",
    status_code=status.HTTP_204_NO_CONTENT
)
async def logout(
        body: TokenSchema,
        service: AuthServiceDep
):
    await service.logout(body)


@router.post(
    "/refresh",
    summary="Обновление токенов",
    status_code=status.HTTP_201_CREATED,
)
async def refresh(
        body: TokenSchema,
        service: AuthServiceDep
):
    response = await service.refresh(body)
    return response


