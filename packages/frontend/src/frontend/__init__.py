import subprocess  # nosec # noqa: S404
import sys

from .settings import Settings


def run_streamlit() -> None:
    args = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(Settings.ENTRYPOINT),
        "--server.port",
        str(Settings.PORT),
        "--server.headless",
        "true",
    ]

    subprocess.run(  # nosec # noqa: S603
        args,
        check=True,
    )


__all__ = ["run_streamlit"]

__version__ = "0.1.2"
