"""LLM helper utilities."""

from __future__ import annotations

from typing import Any, Dict, List

from openai import OpenAI

from app.config import settings


class LLMService:
    """Lightweight wrapper around the OpenAI client with safe defaults."""

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or settings.openai_api_key
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def summarize_event(self, source: str, payload: Dict[str, Any]) -> str:
        """Return a concise summary of an incoming event."""

        if not self.client:
            return f"Event from {source} with payload keys: {', '.join(payload.keys())}"

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Summarize the event for logging and routing decisions.",
                },
                {
                    "role": "user",
                    "content": f"Source: {source}\nPayload: {payload}",
                },
            ],
            max_tokens=120,
            temperature=0,
        )
        return response.choices[0].message.content

    def suggest_tasks(self, intent: str, context: Dict[str, Any] | None = None) -> List[str]:
        """Generate suggested tasks for a given intent."""

        context_str = f" Context: {context}" if context else ""
        if not self.client:
            return [f"Follow up on: {intent}."]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide actionable follow-up tasks."},
                {
                    "role": "user",
                    "content": f"Intent: {intent}.{context_str}",
                },
            ],
            max_tokens=200,
            temperature=0.3,
        )
        return [choice.message.content for choice in response.choices]
