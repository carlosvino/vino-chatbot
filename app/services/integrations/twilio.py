"""Stub Twilio integration."""

from __future__ import annotations


class TwilioClient:
    """Placeholder SMS sender."""

    def send_sms(self, phone_number: str, message: str) -> bool:
        if not phone_number:
            return False
        # A real implementation would call Twilio's REST API.
        print(f"Sending SMS to {phone_number}: {message}")
        return True
