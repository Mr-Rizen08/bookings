from fastapi import APIRouter, Depends

from dependencies.auth import check_for_admin

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(check_for_admin)],
)

#domain/admin/*


