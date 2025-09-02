from typing import Annotated

from core.domain import PredictionInput
from dependency_injector.wiring import inject
from fastapi import APIRouter, Body

from api.dependencies import PredictionServiceDependency

from .examples import EXAMPLES
from .schemas import PredictionRequest, PredictionResponse

router = APIRouter(prefix="/prediction", tags=["Prediction"])


@router.post("/predict")
@inject
async def predict(
    prediction_request: Annotated[PredictionRequest, Body(openapi_examples=EXAMPLES)],
    prediction_service: PredictionServiceDependency,
) -> PredictionResponse:
    prediction_input = PredictionInput(age=prediction_request.input_)
    prediction_output = prediction_service.predict(prediction_input)
    return PredictionResponse(result=prediction_output.time_for_failure)
