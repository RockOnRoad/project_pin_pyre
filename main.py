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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
