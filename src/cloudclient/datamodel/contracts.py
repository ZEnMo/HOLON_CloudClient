from pydantic import BaseModel, Extra

from typing import Optional
from enum import Enum


class ContractTypeEnum(Enum):
    # Contracts to energysupplier
    default = "DEFAULT"
    fixed = "FIXED"
    variable = "VARIABLE"
    dynanmicdayahead = "DYNANMICDAYAHEAD"
    # Contracts to gridoperator
    gopacs = "GOPACS"
    nonfirmato = "NONFIRMATO"
    nodalpricing = "NODALPRICING"


class ContractScopeEnum(Enum):
    energysupplier = "ENERGYSUPPLIER"
    gridoperator = "GRIDOPERATOR"
    energyholon = "ENERGYHOLON"
    administrativeholon = "ADMINISTRATIVEHOLON"


class Contract(BaseModel, extra=Extra.allow):
    type: ContractTypeEnum
    contract_scope: ContractScopeEnum
    # nfATO_capacity_kW: Optional[float]
    # nfATO_starttime_h: Optional[float]
    # nfATO_endtime_h: Optional[float]
