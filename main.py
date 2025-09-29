<<<<<<< HEAD
from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from api_1 import router as rtr_1

from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="service-pin_pyre", lifespan=lifespan)
app.include_router(router=rtr_1, prefix=settings.api_1_prefix)


def main():
    print("Hello from pin-pyre!")
=======
from enum import Enum

from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter

from api.routers import router as rtr

app = FastAPI(title="service-pin_pyre")

main_api_router = APIRouter()

main_api_router.include_router(rtr)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
>>>>>>> 0ff5b33 (0.1.0)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
