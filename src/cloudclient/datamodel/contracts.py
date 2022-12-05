from pydantic import BaseModel, Extra
from enum import Enum


class ContractTypeEnum(Enum):
    # Contracts to energysupplier
    default = "DEFAULT"
    fixed = "FIXED"
    variable = "VARIABLE"
    dynanmicdayahead = "DYNANMICDAYAHEAD"
    # Contracts to gridoperator
    gopacs = "GOPACS"
    nonfirm = "NONFIRM"
    nodalpricing = "NODALPRICING"


class ContractScopeEnum(Enum):
    energysupplier = "ENERGYSUPPLIER"
    gridoperator = "GRIDOPERATOR"
    energyholon = "ENERGYHOLON"
    administrativeholon = "ADMINISTRATIVEHOLON"


class Contract(BaseModel, extra=Extra.forbid):
    type: ContractTypeEnum
    contract_scope: ContractScopeEnum
