"""Routes for ingesting external events."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_session
from app.models import Event
from app.schemas import EventCreate, EventRead

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.post("/events", response_model=EventRead, status_code=status.HTTP_201_CREATED)
def create_event(event: EventCreate, db: Session = Depends(get_session)) -> Event:
    """Persist an inbound event and return the stored record."""

    db_event = Event(source=event.source, payload=event.payload)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


@router.get("/events", response_model=list[EventRead])
def list_events(db: Session = Depends(get_session)) -> list[Event]:
    """Return a list of recent events."""

    return db.query(Event).order_by(Event.created_at.desc()).all()


@router.get("/events/{event_id}", response_model=EventRead)
def get_event(event_id: int, db: Session = Depends(get_session)) -> Event:
    """Fetch a single event by id."""

    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return event
