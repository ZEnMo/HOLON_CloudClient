from enum import Enum
from typing import Optional

from cloudclient.datamodel.assets.energy import EnergyAsset


class ConsumptionAssetTypeEnum(Enum):
    electricity_demand = "ELECTRICITY_DEMAND"
    electric_hob = "ELECTRIC_HOB"
    heat_demand = "HEAT_DEMAND"
    hot_water_consumption = "HOT_WATER_CONSUMPTION"
    other_electricity_consumption = "OTHER_ELECTRICITY_CONSUMPTION"


class ConsumptionAsset(EnergyAsset):
    category = "CONSUMPTION"
    type: ConsumptionAssetTypeEnum
    name: str

class HeatConsumptionAsset(ConsumptionAsset):
    yearlyDemandHeat_kWh: float


class ElectricConsumptionAsset(ConsumptionAsset):
    yearlyDemandElectricity_kWh = 0.0


class HybridConsumptionAsset(ElectricConsumptionAsset, HeatConsumptionAsset):
    pass
