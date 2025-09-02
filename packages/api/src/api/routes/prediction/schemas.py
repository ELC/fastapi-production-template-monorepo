from pydantic import Field

from api.schema import BaseSchema


class PredictionRequest(BaseSchema):
    input_: float = Field(alias="input", gt=0)


class PredictionResponse(BaseSchema):
    result: float
