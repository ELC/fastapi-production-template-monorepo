from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    PORT: int = 10000
    HOST: str = "0.0.0.0"  # nosec  # noqa: S104

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def APP_PATH(self) -> Path:
        return Path(__file__).resolve().parent

    @property
    def ENTRYPOINT(self) -> Path:
        return self.APP_PATH / "home.py"


Settings = _Settings()
