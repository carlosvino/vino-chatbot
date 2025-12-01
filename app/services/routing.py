"""Routing service for deciding how to process events."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

from app.models import Event
from app.services.llm import LLMService


@dataclass
class RoutingDecision:
    summary: str
    suggested_tasks: List[str]


class RoutingService:
    """Use heuristics and LLM assistance to route events into tasks."""

    def __init__(self, llm: LLMService | None = None) -> None:
        self.llm = llm or LLMService()

    def process_event(self, event: Event | Dict[str, Any]) -> RoutingDecision:
        source = event.source if isinstance(event, Event) else event.get("source", "unknown")
        payload = event.payload if isinstance(event, Event) else event.get("payload", {})

        summary = self.llm.summarize_event(source=source, payload=payload)
        suggested_tasks = self.llm.suggest_tasks(intent=summary, context=payload)
        return RoutingDecision(summary=summary, suggested_tasks=suggested_tasks)
