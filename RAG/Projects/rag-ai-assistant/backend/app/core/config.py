from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import List


class Settings(BaseSettings):
    PROJECT_NAME: str = "RAG AI Assistant"
    API_V1_STR: str = "/api"
    ALLOWED_ORIGINS: List[str] = ["*"]

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()
