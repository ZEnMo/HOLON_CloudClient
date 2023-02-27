from cloudclient.datamodel.assets.energy import EnergyAsset, AmbientTempTypeEnum
from enum import Enum
from typing import Optional


class StorageAssetTypeEnum(Enum):
    electric_vehicle = "ELECTRIC_VEHICLE"
    storage_electric = "STORAGE_ELECTRIC"
    storage_heat = "STORAGE_HEAT"
    heatmodel = "HEATMODEL"


class StorageAsset(EnergyAsset):
    category = "STORAGE"
    type: StorageAssetTypeEnum
    name: str


class HeatStorageAsset(StorageAsset):
    capacityHeat_kW: float
    #stateOfCharge_r: float
    initial_temperature_degC: float
    minTemp_degC: int
    maxTemp_degC: int
    setTemp_degC: int
    lossFactor_WpK: float
    heatCapacity_JpK: float
    ambientTempType: AmbientTempTypeEnum

class ElectricStorageAsset(StorageAsset):
    capacityElectricity_kW: float
    stateOfCharge_r: float
    storageCapacity_kWh: float

class VehicleElectricStorageAsset(ElectricStorageAsset):
    energyConsumption_kWhpkm: float
    vehicleScaling: int
