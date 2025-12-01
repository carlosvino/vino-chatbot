"""Simple worker to demonstrate event processing pipeline."""

from __future__ import annotations

from typing import Iterable

from app.models import Event, Task
from app.services import RoutingService
from app.services.integrations import CalendarClient, GmailClient, TwilioClient


class EventProcessor:
    """Process events and fan out to integrations."""

    def __init__(
        self,
        routing: RoutingService | None = None,
        gmail: GmailClient | None = None,
        sms: TwilioClient | None = None,
        calendar: CalendarClient | None = None,
    ) -> None:
        self.routing = routing or RoutingService()
        self.gmail = gmail or GmailClient()
        self.sms = sms or TwilioClient()
        self.calendar = calendar or CalendarClient()

    def process(self, event: Event) -> list[Task]:
        """Return tasks that should be created for a given event."""

        decision = self.routing.process_event(event)
        tasks: list[Task] = []
        for suggestion in decision.suggested_tasks:
            task = Task(title=suggestion, status="pending")
            tasks.append(task)
        return tasks

    def notify(self, message: str, recipients: Iterable[str]) -> None:
        """Send notifications via email and SMS."""

        self.gmail.send_email(recipients, subject="Titan-SI Notification", body=message)
        for recipient in recipients:
            self.sms.send_sms(recipient, message)
