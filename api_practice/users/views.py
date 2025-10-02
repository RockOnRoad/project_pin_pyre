from fastapi import APIRouter

from .schemas import CreateUser
from ..users import crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def root():
    return {"message": "users router"}


@router.post("/")
async def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
