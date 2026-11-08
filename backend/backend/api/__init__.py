from fastapi import APIRouter

from backend.api.v1.catalog import catalog_router
from backend.api.v1.auth import router as auth_router
from backend.api.v1.user import router as user_router
from backend.api.v1.admin import router as admin_router

v1_router = APIRouter(
    prefix="/api/v1"
)

v1_router.include_router(catalog_router)
v1_router.include_router(auth_router)
v1_router.include_router(user_router)
v1_router.include_router(admin_router)

