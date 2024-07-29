from fastapi import APIRouter

from api.products import router as products_router

router = APIRouter(
    prefix="/api",
)
router.include_router(products_router)
