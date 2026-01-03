from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    neon_database_url: str
    qdrant_api_key: str
    qdrant_host: str
    cohere_api_key: str
    gemini_api_key: str
    gemini_base_url: str

    class Config:
        env_file = ".env"

settings = Settings()
