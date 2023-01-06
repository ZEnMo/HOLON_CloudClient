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


class SubTypeEnum(Enum):
    commercial = "commercial"


class Actor(BaseModel, extra=Extra.forbid):
    category: ActorTypeEnum
    type: Optional[SubTypeEnum]
    id: str
    parent_actor: str
    contracts: Optional[List[Contract]]


# class NonFirmActor(Actor):
#     nfATO_capacity_kw: float
#     nfATO_starttime: float
#     nfATO_endtime: float
