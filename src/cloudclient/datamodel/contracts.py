from pydantic import BaseModel, Extra

from typing import Optional
from enum import Enum


# # Contracts to gridoperator
# gopacs = "GOPACS"
# nonfirmato = "NONFIRMATO"
# nodalpricing = "NODALPRICING"


# class ContractScopeEnum(Enum):
#     energysupplier = "ENERGYSUPPLIER"
#     gridoperator = "GRIDOPERATOR"
#     energyholon = "ENERGYHOLON"
#     administrativeholon = "ADMINISTRATIVEHOLON"


class EnergyCarrierEnum(Enum):
    electricity = "ELECTRICITY"
    heat = "HEAT"
    methane = "METHANE"
    hydrogen = "HYDROGEN"
    diesel = "DIESEL"


class ContractTypeEnum(Enum):
    delivery = "DELIVERY"
    transport = "TRANSPORT"
    connection = "CONNECTION"
    tax = "TAX"


class Contract(BaseModel, extra=Extra.forbid):
    contractType: ContractTypeEnum
    contractScope: str
    energyCarrier: EnergyCarrierEnum
    annualFee_eur = 0.0


class DeliveryContractTypeEnum(Enum):
    fixed = "ELECTRICITY_FIXED"
    variable = "ELECTRICITY_VARIABLE"


class DeliveryContract(Contract):
    contractType = ContractTypeEnum.delivery
    deliveryContractType: DeliveryContractTypeEnum
    deliveryPrice_eurpkWh: float
    feedinPrice_eurpkWh: float


class ConnectionContractTypeEnum(Enum):
    default = "DEFAULT"
    nfATO = "NFATO"


class ConnectionContract(Contract):
    contractType = ContractTypeEnum.connection
    connectionContractType: ConnectionContractTypeEnum
    nfATO_capacity_kW = 0.0
    nfATO_starttime_h = 0.0
    nfATO_endtime_h = 0.0


class TaxContractTypeEnum(Enum):
    salderen = "SALDEREN"
    nietsalderen = "NIETSALDEREN"


class TaxContract(Contract):
    contractType = ContractTypeEnum.tax
    taxContractType: TaxContractTypeEnum
    taxDelivery_eurpkWh: float
    taxFeedin_eurpkWh: float
    proportionalTax_pct: float


class TransportContractTypeEnum(Enum):
    default = "DEFAULT"
    nodalpricing = "NODALPRICING"
    bandwidth = "BANDWIDTH"


class TransportContract(Contract):
    contractType = ContractTypeEnum.transport
    transportContractType: TransportContractTypeEnum
    bandwidthTreshold_kW = 0.0
    bandwidthTariff_eurpkWh = 0.0
