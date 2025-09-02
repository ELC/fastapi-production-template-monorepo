import pytest

from core.injections import configure_container
from core.injections.test import TestContainer


@pytest.fixture(autouse=True, scope="session")
def injector_override() -> None:
    container = configure_container()
    container.override(TestContainer)
    container.wire(packages=["tests"])  # pylint: disable=no-member
