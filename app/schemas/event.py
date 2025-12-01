"""Schemas for event ingestion."""

from datetime import datetime
from typing import Any, Dict

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class EventBase(BaseModel):
    source: str = Field(..., description="Originating system of the event")
    payload: Dict[str, Any] = Field(default_factory=dict, description="Raw event payload")


class EventCreate(EventBase):
    """Incoming event payload."""


class EventRead(EventBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
