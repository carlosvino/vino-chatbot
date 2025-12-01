"""Database session and metadata configuration."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

engine = create_engine(settings.database_url, future=True, echo=False)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
Base = declarative_base()


def get_session():
    """Provide a database session for dependency injection."""

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
