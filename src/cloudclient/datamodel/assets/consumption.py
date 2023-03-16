from enum import Enum
from typing import Optional

from cloudclient.datamodel.assets.energy import EnergyAsset


class ConsumptionAssetTypeEnum(Enum):
    electricity_demand = "ELECTRICITY_DEMAND"
    heat_demand = "HEAT_DEMAND"
    hot_water_consumption = "HOT_WATER_CONSUMPTION"
    other_electricity_consumption = "OTHER_ELECTRICITY_CONSUMPTION"
    diesel_vehicle = "DIESEL_VEHICLE"
    electric_hob = "ELECTRIC_HOB"


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

class DieselVehicleAsset(ConsumptionAsset):
    name : str
    energyConsumption_kWhpkm = 0.8
    type = ConsumptionAssetTypeEnum.diesel_vehicle
    vehicleScaling = 1

class ElectricHob(ElectricConsumptionAsset):
    capacityElectricity_kW: float
