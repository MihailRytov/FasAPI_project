from pydantic_settings import BaseSettings

DATABASE_URL: str = "postgresql+asyncpg://admin:admin@localhost/servicebase"


class Setting(BaseSettings):
    db_url: str = DATABASE_URL
    db_echo: bool = True


settings = Setting()
