from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_1_prefix: str = "/api/v1"

    db_url: str = "postgresql+asyncpg://postgres:postgres@192.168.10.46:5432/postgres"
    db_echo: bool = False


settings = Settings()
