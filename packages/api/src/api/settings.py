from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    PORT: int = 8000
    HOST: str = "0.0.0.0"  # nosec  # noqa: S104

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Settings = _Settings()
