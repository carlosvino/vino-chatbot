"""Stub calendar integration."""

from __future__ import annotations

from datetime import datetime


class CalendarClient:
    """Placeholder calendar client for scheduling."""

    def create_event(self, title: str, start: datetime, end: datetime) -> bool:
        if not title:
            return False
        # A real implementation would push events to Google Calendar or Outlook.
        print(f"Creating calendar event '{title}' from {start} to {end}")
        return True
