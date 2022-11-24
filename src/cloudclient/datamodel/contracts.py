from pydantic import BaseModel, Extra
from enum import Enum


class ContractTypeEnum(Enum):
    default = "DEFAULT"
    variable = "VARIABLE"
    dynanmicdayahead = "DYNANMICDAYAHEAD"
    gopacs = "GOPACS"
    nonfirm = "NONFIRM"


class ContractScopeEnum(Enum):
    energysupplier = "ENERGYSUPPLIER"
    gridoperator = "GRIDOPERATOR"
    energyholon = "ENERGYHOLON"
    administrativeholon = "ADMINISTRATIVEHOLON"


class Contract(BaseModel, extra=Extra.forbid):
    type: ContractTypeEnum
    contract_scope: ContractScopeEnum
