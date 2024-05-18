from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_URL: str = f"sqlite+aiosqlite:///{BASE_DIR}/servicebase"


class Setting(BaseSettings):
    api_v1_prefix: str = "/api/v1/"
    db_url: str = DATABASE_URL
    db_echo: bool = True


settings = Setting()
