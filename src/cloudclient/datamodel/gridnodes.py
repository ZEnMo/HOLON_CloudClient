from pydantic import BaseModel, Extra
from typing import Optional

from enum import Enum


class EnergyTypeEnum(Enum):
    electricity = "ELECTRICITY"
    heat = "HEAT"


class GridNode(BaseModel, extra=Extra.forbid):
    owner_actor: str
    id: str
    capacity_kw: float
    parent: Optional[str]


class ElectricGridTypeEnum(Enum):
    msls = "MSLS"
    hsms = "HSMS"


class ElectricGridNode(GridNode):
    type: ElectricGridTypeEnum
    category = "ELECTRICITY"


class HeatGridTypeEnum(Enum):
    lt = "LT"
    mt = "MT"
    ht = "HT"


class HeatGridNode(GridNode):
    type: HeatGridTypeEnum
    category = "HEAT"
    assets = []
