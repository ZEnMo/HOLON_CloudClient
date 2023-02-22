from cloudclient.datamodel.assets.energy import EnergyAsset
from enum import Enum
from typing import Optional


class ProductionAssetTypeEnum(Enum):
    photovoltaic = "PHOTOVOLTAIC"
    windmill = "WINDMILL"
    residualheatHT = "RESIDUALHEATHT"
    residualheatLT = "RESIDUALHEATLT"


    

class ProductionAsset(EnergyAsset):
    category = "PRODUCTION"
    type: ProductionAssetTypeEnum
    name: str


class ElectricProductionAsset(ProductionAsset):
    capacityElectricity_kW: float


class HeatProductionAsset(ProductionAsset):
    capacityHeat_kW: float
    deliveryTemp_degC: float


class HybridProductionAsset(ElectricProductionAsset, HeatProductionAsset):
    pass
