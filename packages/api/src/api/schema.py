from core.utils import ExamplerMixIn
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class BaseSchema(BaseModel, ExamplerMixIn):
    model_config = ConfigDict(alias_generator=to_camel, arbitrary_types_allowed=True)
