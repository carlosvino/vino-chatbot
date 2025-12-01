# Titan-SI

An event-ingestion and task-routing service powered by FastAPI. The project layout is designed for clean separation between API routes, services, database models, and background workers.

## Project structure

```
titan-si/
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── config.py            # Settings management
│   ├── db.py                # SQLAlchemy engine + session
│   ├── models/              # ORM models
│   ├── schemas/             # Pydantic schemas
│   ├── routers/             # FastAPI routers
│   ├── services/            # LLM and integration services
│   └── workers/             # Background processing utilities
├── alembic/                 # Database migrations
│   └── versions/            # Generated migration files
├── tests/                   # Pytest suite
├── .env.example             # Example environment variables
├── requirements.txt         # Runtime dependencies
└── README.md
```

## Getting started

1. **Install dependencies**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure environment**

   Copy the example environment file and update values as needed:

   ```bash
   cp .env.example .env
   ```

3. **Run database migrations** (optional for SQLite)

   With Alembic installed you can generate and apply migrations:

   ```bash
   alembic revision --autogenerate -m "init"
   alembic upgrade head
   ```

4. **Start the API server**

   ```bash
   uvicorn app.main:app --reload
   ```

   Visit `http://localhost:8000/docs` for interactive documentation.

## Testing

The `tests/` folder is ready for Pytest-based tests. Add new test modules as features are implemented.

## Architecture

See [docs/titan_si_integration_architecture.md](docs/titan_si_integration_architecture.md) for the high-level integration architecture and MVP build plan.
