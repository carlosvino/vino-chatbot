"""API routers."""

from fastapi import APIRouter

from app.routers import ingest, tasks

api_router = APIRouter()
api_router.include_router(ingest.router)
api_router.include_router(tasks.router)

__all__ = ["api_router"]
