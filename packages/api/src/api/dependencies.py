from typing import Annotated

from core.services import PredictionService, TrainingService
from dependency_injector.wiring import Provide
from fastapi import Depends

PredictionServiceDependency = Annotated[
    PredictionService,
    Depends(Provide["prediction_service"]),
]

TrainingServiceDependency = Annotated[
    TrainingService,
    Depends(Provide["training_service"]),
]
