from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def APP_PATH(self) -> Path:
        return Path(__file__).resolve().parent

    @property
    def MODEL_DIRECTORY(self) -> Path:
        model_directory = self.APP_PATH / "ml_binaries"
        model_directory.mkdir(parents=True, exist_ok=True)
        return model_directory

    @property
    def MODEL_PATH(self) -> Path:
        return self.MODEL_DIRECTORY / "model.joblib"


Settings = _Settings()
