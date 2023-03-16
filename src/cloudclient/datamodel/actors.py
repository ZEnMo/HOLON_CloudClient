from pydantic import BaseModel, Extra
from enum import Enum
from typing import Optional, List
from cloudclient.datamodel.contracts import Contract


class ActorTypeEnum(Enum):
    gridoperator = "GRIDOPERATOR"
    administrativeholon = "ADMINISTRATIVEHOLON"
    energyholon = "ENERGYHOLON"
    connectionowner = "CONNECTIONOWNER"
    energysupplier = "ENERGYSUPPLIER"


class Actor(BaseModel):
    category: ActorTypeEnum
    group: str
    subgroup = ""
    id: str
    contracts = []  # Optional[List[Contract]]
    node = ""


# class SubTypeEnum(Enum):
#     commercial = "commercial"


# class NonFirmActor(Actor):
# nfATO_capacity_kw: float
# nfATO_starttime: float
# nfATO_endtime: float
