from collections.abc import Callable

from core.services.training import DimensionalityMismatchError
from fastapi import Request, Response

from .training import dimensionality_mismatch_handler

ExceptionHandler = Callable[[Request, Exception], Response]

EXCEPTION_HANDLERS: dict[type[Exception], ExceptionHandler] = {
    DimensionalityMismatchError: dimensionality_mismatch_handler,  # type: ignore[dict-item]
}

__all__ = ["EXCEPTION_HANDLERS"]
