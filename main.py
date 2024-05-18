from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from core.database import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
