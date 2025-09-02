from core.services.training import DimensionalityMismatchError
from fastapi import Request
from fastapi.responses import JSONResponse


def dimensionality_mismatch_handler(
    _: Request,
    exc: DimensionalityMismatchError,
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )
