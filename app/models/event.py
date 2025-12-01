"""Event model definition."""

from datetime import datetime

from sqlalchemy import JSON, Column, DateTime, Integer, String

from app.db import Base


class Event(Base):
    """Persistent representation of an inbound event."""

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(100), nullable=False)
    payload = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<Event id={self.id} source={self.source}>"
