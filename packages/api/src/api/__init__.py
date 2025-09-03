import uvicorn

from .app import create_app
from .settings import Settings


def run_api() -> None:
    uvicorn.run(
        "api:create_app",
        factory=True,
        host=Settings.HOST,
        port=Settings.PORT,
    )


__all__ = ["create_app", "run_api"]

__version__ = "0.2.0"
