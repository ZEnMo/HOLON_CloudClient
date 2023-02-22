from pydantic import BaseModel, Extra

from typing import Optional
from enum import Enum


class ContractTypeEnum(Enum):
    delivery = "DELIVERY"
    transport = "TRANSPORT"
    connection = "CONNECTION"
    tax = "TAX"
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


class DeliveryContractTypeEnum(Enum):
    fixed = "ELECTRICITY_FIXED"
    variable = "ELECTRICITY_VARIABLE"


class ConnectionContractTypeEnum(Enum):
    default = "DEFAULT"
    nfATO = "NFATO"


class TransportContractTypeEnum(Enum):
    default = "DEFAULT"
    nodalpricing = "NODALPRICING"
    peak = "PEAK"
    bandwidth = "BANDWIDTH"


class TaxContractTypeEnum(Enum):
    salderen = "SALDEREN"
    nietsalderen = "NIETSALDEREN"


class Contract(BaseModel, extra=Extra.forbid):
    contractType: ContractTypeEnum
    contractScope: str
    energyCarrier: EnergyCarrierEnum
    deliveryContractType: Optional[DeliveryContractTypeEnum]
    deliveryPrice_eurpkWh: Optional[float]
    feedinPrice_eurpkWh: Optional[float]
    annualFee_eur: Optional[float]
    connectionContractType: Optional[ConnectionContractTypeEnum]
    nfATO_capacity_kW: Optional[float]
    nfATO_starttime_h: Optional[float]
    nfATO_endtime_h: Optional[float]

    taxContractType: Optional[TaxContractTypeEnum]
    taxDelivery_eurpkWh: Optional[float]
    taxFeedin_eurpkWh: Optional[float]
    proportionalTax_pct: Optional[float]

    transportContractType: Optional[TransportContractTypeEnum]
    bandwidthTreshold_kW: Optional[float]
    bandwidthTariff_eurpkWh: Optional[float]
