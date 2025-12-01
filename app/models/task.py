"""Task model definition."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.db import Base


class Task(Base):
    """Task representation with simple status tracking."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    status = Column(String(50), default="pending", nullable=False)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<Task id={self.id} title={self.title}>"
