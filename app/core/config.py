"""Application configuration."""

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    
    app_name: str = "Items API"
    app_version: str = "1.0.0"
    app_description: str = "A simple CRUD API for managing items"
    
    # API settings
    api_host: str = "127.0.0.1"
    api_port: int = 3400
    
    # Storage settings
    data_file: str = "data/data.json"
    
    # Optional fields from .env (for langchain compatibility)
    openai_api_key: Optional[str] = None
    openai_model: Optional[str] = None
    brave_api_key: Optional[str] = None
    tavily_api_key: Optional[str] = None
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
