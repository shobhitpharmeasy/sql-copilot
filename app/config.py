import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Load environment variables from .env file
    class Config:
        env_file = ".env"

    # Example settings
    APP_NAME: str = "SQL Copilot"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    # Add more settings as needed

settings = Settings()
