"""Database session and metadata configuration."""

from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.config import settings

engine = create_engine(settings.database_url, future=True, echo=False)
SessionLocal = sessionmaker(
    bind=engine, autocommit=False, autoflush=False, class_=Session, future=True
)
Base = declarative_base()


def get_session() -> Iterator[Session]:
    """Provide a database session for dependency injection."""

    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
