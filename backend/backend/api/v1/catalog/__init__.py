from fastapi import APIRouter

from backend.api.v1.catalog.masters import router as masters_router
from backend.api.v1.catalog.services import router as services_router


catalog_router = APIRouter(
    tags=["catalog"]
)

catalog_router.include_router(masters_router)
catalog_router.include_router(services_router)
