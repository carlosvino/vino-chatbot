"""FastAPI entrypoint for Titan-SI."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import Base, engine
from app.routers import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Prepare application resources for the API lifecycle."""

    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Titan-SI", version="0.1.0", lifespan=lifespan)
app.include_router(api_router)


@app.get("/health", tags=["health"])
def healthcheck() -> dict[str, str]:
    """Simple health endpoint."""

    return {"status": "ok"}
