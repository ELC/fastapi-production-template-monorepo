from collections.abc import Sequence
from typing import Self

from core.services.training import DimensionalityMismatchError
from pydantic import model_validator

from api.schema import BaseSchema


class TrainRequest(BaseSchema):
    age: Sequence[Sequence[float]]
    time_for_failure: Sequence[float]

    @model_validator(mode="after")
    def features_and_labels_have_same_length(self) -> Self:
        if len(self.age) != len(self.time_for_failure):
            raise DimensionalityMismatchError(
                x_dim=len(self.age),
                y_dim=len(self.time_for_failure),
            )
        return self


class TrainResponse(BaseSchema): ...
