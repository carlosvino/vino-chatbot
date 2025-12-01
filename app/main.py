"""FastAPI entrypoint for Titan-SI."""

from __future__ import annotations

from fastapi import FastAPI

from app.db import Base, engine
from app.routers import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Titan-SI", version="0.1.0")
app.include_router(api_router)


@app.get("/health", tags=["health"])
def healthcheck() -> dict[str, str]:
    """Simple health endpoint."""

    return {"status": "ok"}
