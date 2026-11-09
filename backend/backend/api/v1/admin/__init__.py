from fastapi import APIRouter, Depends
from dependencies.auth import check_for_admin
from backend.api.v1.admin.user import router as user_router
from backend.api.v1.admin.service import router as service_router
from backend.api.v1.admin.master import router as master_router
router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(check_for_admin)],
)

#domain/admin/*
router.include_router(user_router)
router.include_router(service_router)
router.include_router(master_router)
