from fastapi import APIRouter

from .products.views import router as products_rtr

router = APIRouter()
router.include_router(router=products_rtr, prefix="/products")
