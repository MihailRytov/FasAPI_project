from pydantic_settings import BaseSettings

DATABASE_URL: str = "postgresql+asyncpg://admin:admin@localhost/servicebase"


class Setting(BaseSettings):
    db_url: str = DATABASE_URL


settings = Setting()
