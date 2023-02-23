from enum import Enum
from typing import Optional

from cloudclient.datamodel.assets.energy import EnergyAsset


class ConsumptionAssetTypeEnum(Enum):
    electricity_demand = "ELECTRICITY_DEMAND"
    diesel_vehicle = "DIESEL_VEHICLE"
    heat_demand = "HEAT_DEMAND"
    hot_water_consumption = "HOT_WATER_CONSUMPTION"
    other_electricity_consumption = "OTHER_ELECTRICITY_CONSUMPTION"


class ConsumptionAsset(EnergyAsset):
    category = "CONSUMPTION"
    type: ConsumptionAssetTypeEnum
    name: str


class DieselVehicleAsset(ConsumptionAsset):
    energyConsumption_kWhpkm = 0.8
    type = ConsumptionAssetTypeEnum.diesel_vehicle
    vehicleScaling = 1


class HeatConsumptionAsset(ConsumptionAsset):
    yearlyDemandHeat_kWh: float


class ElectricConsumptionAsset(ConsumptionAsset):
    yearlyDemandElectricity_kWh = 0.0


class HybridConsumptionAsset(ElectricConsumptionAsset, HeatConsumptionAsset):
    pass
