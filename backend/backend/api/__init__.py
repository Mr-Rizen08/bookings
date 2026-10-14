from fastapi import APIRouter

from api.v1.catalog import catalog_router

v1_router  =APIRouter(
    prefix="/api/v1"
)

v1_router.include_router(catalog_router)

