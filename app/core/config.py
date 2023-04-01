from typing import List
from fastapi import FastAPI
from pydantic import BaseSettings, validator

class Settings(BaseSettings):
    PROJECT_NAME: str = "My Property Management App"
    PROJECT_DESCRIPTION: str = "A simple API for property management"
    PROJECT_VERSION: str = "0.1.0"
    
    DATABASE_URL: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    
    class Config:
        env_file = ".env"

    @validator("DATABASE_URL", pre=True)
    def check_database_url(cls, v: str) -> str:
        """Check if the database URL starts with 'sqlite:///'.

        Args:
            v (str): The database URL to be validated.

        Returns:
            str: The validated database URL.

        Raises:
            ValueError: If the database URL does not start with 'sqlite:///'.
        """
        if not v.startswith("sqlite:///"):
            raise ValueError("only sqlite is supported")
        return v

settings = Settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)
