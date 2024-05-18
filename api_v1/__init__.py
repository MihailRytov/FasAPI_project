from fastapi import APIRouter

from .servicebase.views import router as brand_router

router = APIRouter()
router.include_router(router=brand_router, prefix="/brands/")
