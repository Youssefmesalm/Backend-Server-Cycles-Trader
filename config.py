from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from pydantic import Field
import secrets


class Settings(BaseSettings):
    # Secrets
    secret_key: str = Field(default_factory=lambda: str(secrets.token_hex(32)))
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24 * 3  # 3 days
    refresh_token_expire_minutes: int = 60 * 24 * 15  # 15 days
    local_token_expire_minutes: int = 60 * 24 * 30 * 12 + 5  # 365 days
    # DB
    db_name: str = "database.sqlite"
    db_echo: bool = False

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

if __name__ == "__main__":
    print(settings)
