"""Configuration management for Titan-SI."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env."""

    model_config = SettingsConfigDict(env_file=".env")

    database_url: str = Field(
        default="sqlite:///./titan_si.db",
        alias="DATABASE_URL",
        description="SQLAlchemy database URL",
    )
    openai_api_key: str | None = Field(default=None, alias="OPENAI_API_KEY")


settings = Settings()
