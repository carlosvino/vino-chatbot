"""Stub Gmail integration for notifications."""

from __future__ import annotations

from typing import Iterable, List


class GmailClient:
    """Placeholder client showing how email delivery would be wired."""

    def send_email(self, recipients: Iterable[str], subject: str, body: str) -> bool:
        recipient_list: List[str] = list(recipients)
        if not recipient_list:
            return False
        # This is a placeholder; real implementation would call Gmail/SMTP APIs.
        print(f"Sending email to {', '.join(recipient_list)}: {subject}\n{body}")
        return True
