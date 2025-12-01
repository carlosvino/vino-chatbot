"""Schemas for task management."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class TaskBase(BaseModel):
    title: str = Field(..., description="Summary of the task")
    status: str = Field(default="pending", description="Current task status")
    due_date: Optional[datetime] = Field(default=None, description="Optional due date")


class TaskCreate(TaskBase):
    """Payload for creating tasks."""


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None


class TaskRead(TaskBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
