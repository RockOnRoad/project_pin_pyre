from fastapi import APIRouter

from .users import router as users_rtr

router = APIRouter(prefix="")
router.include_router(users_rtr)


@router.get("/")
async def root():
    return {"message": "Hello World"}
