# Titan SI Integration Architecture & MVP Build Plan

This document captures the integration architecture and MVP build plan for Titan SI, a founder-focused superintelligence designed to capture, organize, and act upon every input in an entrepreneur’s life. It summarizes the high-level blueprint, system layers, core objects, and phased development plan discussed in earlier conversations.

## System Overview

Titan SI comprises five core layers that transform raw inputs into actionable insights and tasks:

1. **Interface Layer** – Dashboards, daily briefings, and chat bot for user interaction.
2. **Action Layer** – Handles task routing, drafting emails, calendar updates, and other automations.
3. **Decision Layer** – Applies priority scoring, mental load, and routing logic to determine what matters now.
4. **AI Understanding Layer** – Uses LLMs and classifiers to parse transcripts, emails, and messages, extracting tasks, commitments, entities, and sentiment.
5. **Capture Layer** – Ingests calls, SMS, emails, calendar events, health data, and third-party tool events. Data flows into the Titan Data Platform, a data lake that stores raw events, transcripts, and structured objects.

## Universal Connect Engine

Titan SI is platform-agnostic. The integration architecture supports multiple connectivity methods so that founders can use any tools or no tools at all:

- **Direct API Connectors** – OAuth-based connectors to common CRMs, project management tools, email providers, and health APIs.
- **Email Parsing** – Generic fallback for tools without APIs; Titan monitors notification emails and parses them into structured events.
- **File Integration** – Handles CSV, PDF, or document exports from systems that lack APIs.
- **Screen/RPA Integration** – Uses browser automation and computer vision to interact with legacy systems via the UI.

By standardizing all captured data into a universal founder schema, Titan can map any event or task into the appropriate destination system.

## Core Data Objects (Universal Schema)

The Titan platform normalizes all captured inputs into four foundational objects that can be routed into external tools or stored internally:

- **Event** – Represents an atomic event such as an email, call, SMS, or meeting. Stores raw content, metadata, source type and platform, timestamp, and any initial sentiment or stress signals.
- **Task** – Encodes an actionable item extracted from events. Includes description, priority, due date, status, owner, related contact/project, and whether it is personal.
- **Contact** – Normalized representation of people or organizations. Tracks names, communication details, tags, and relationship type.
- **Project** – Groups tasks and communications under a common initiative; holds project stage, deadlines, and associated insights.

These objects enable Titan to route work into arbitrary external tools or maintain tasks internally when no tool is configured.

## MVP Build Plan

The MVP focuses on delivering tangible value to one founder (the initial user) in 8–12 weeks.

### Goals

- Capture calls, emails, texts, and calendar events.
- Extract tasks, commitments, and summaries via an LLM pipeline.
- Deliver daily briefings and weekly reviews.
- Integrate with at least one project management tool and one CRM, with configurable routing rules.
- Provide a simple web dashboard with a Today view, tasks list, and stress score.

### Core Components

- **Telephony/SMS Integration**: Use Twilio to record calls and capture SMS. Transcribe calls using a speech-to-text service (e.g., Whisper or Deepgram).
- **Email Integration**: Connect to Gmail via OAuth, monitor a Titan label, and sync messages.
- **Calendar Integration**: Read the user’s Google Calendar to understand meeting load and for stress scoring.
- **LLM Processing**: A service that sends raw content to an LLM with a structured system prompt and parses the JSON result into tasks.
- **Task Routing**: A service that creates tasks either in Titan’s internal database or in external systems (CRM/PM) based on routing rules.
- **Daily Briefing Service**: A scheduled process that compiles today’s top priorities, at-risk commitments, and suggestions.
- **Dashboard**: A minimal React or Svelte front-end showing tasks, events, and stress status.

### Tech Stack

- **Backend**: Python 3.11+, FastAPI, SQLAlchemy/Alembic for Postgres migrations, Redis for future queueing, Celery/RQ for background tasks. Use the OpenAI API for LLM calls.
- **Storage**: Postgres for structured data, S3-compatible object storage for recordings/transcripts, and a vector store (e.g., Chroma or Pinecone) for memory in later phases.
- **Frontend**: React or Svelte with Tailwind for UI. The UI is optional for the first iteration; email reports provide initial value.

### Phased Timeline

- **Phase 0 (1–2 weeks)** – Architecture and configuration: set up the repository, database, and authentication flows.
- **Phase 1 (2–3 weeks)** – Capture layer: implement Twilio, Gmail, and Calendar ingestion and store raw events.
- **Phase 2 (2–3 weeks)** – AI layer: implement the LLM extraction service and basic sentiment scoring.
- **Phase 3 (2 weeks)** – Routing layer: build the task router and connectors to one CRM and one PM tool.
- **Phase 4 (1–2 weeks)** – Action layer: implement daily/weekly briefings and a basic Titan Mode (suppress low-priority noise).
- **Phase 5 (2 weeks)** – Dashboard: develop a simple web interface for the founder.

### Notes

The blueprint is intentionally modular so it can be adapted to different toolsets. Future phases will extend the integration layer with more connectors (including RPA), add health monitoring, implement advanced stress analytics, and open the Titan platform as a marketplace.
