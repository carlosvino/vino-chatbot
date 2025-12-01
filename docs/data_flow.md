# Data Flow Overview

The system processes incoming signals through layered stages that ensure each source is captured, interpreted, prioritized, and acted on in downstream tools.

## Pipeline Stages

1. **Incoming Data** – Calls, emails, SMS, meetings, health signals, and CRM/PM tool events enter the system.
2. **Capture Layer** – Webhooks, polling, email ingestion, and RPA connectors normalize and ingest events into the platform.
3. **Data Lake** – Raw events, transcripts, and metadata are stored for durable history and analytics.
4. **AI Understanding Layer** – An LLM parses and classifies events to extract intent, entities, and contextual labels.
5. **Decision Layer** – Rules and scores (priority, stress, routing) determine handling based on business logic.
6. **Action Layer** – Tasks are created or updated, suggestions generated, and automations executed in target systems.
7. **Interface Layer** – Briefings, dashboards, and chat commands expose insights and controls to end users.

## Key Notes

- Each layer can operate asynchronously, enabling replay or reprocessing from the Data Lake when models or rules change.
- Captured metadata flows alongside content to preserve context for classification and routing decisions.
- Actions can be audited end-to-end by tracing an event from ingestion through the interface where users see outcomes.
