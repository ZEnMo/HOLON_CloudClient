from pydantic import BaseModel, Extra
from typing import Optional


class Policy(BaseModel, extra=Extra.forbid):
    parameter: str
    value: str
    unit: Optional[str]
    comment: str
