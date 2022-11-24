from enum import Enum
from cloudclient.datamodel.assets.energy import EnergyAsset, AmbientTempTypeEnum
from typing import Optional


class ConversionAssetTypeEnum(Enum):
    boiler = "BOILER"
    electrolyser = "ELECTROLYSER"
    gas_burner = "GAS_BURNER"
    heat_delivery_set = "HEAT_DELIVERY_SET"
    heat_pump_air = "HEAT_PUMP_AIR"
    heat_pump_ground = "HEAT_PUMP_GROUND"
    hydrogen_furnace = "HYDROGEN_FURNACE"
    methane_furnace = "METHANE_FURNACE"
    diesel_vehicle = "DIESEL_VEHICLE"


class ConversionAsset(EnergyAsset):
    category = "CONVERSION"
    type: ConversionAssetTypeEnum
    eta_r: float
    name: str


class VehicleConversionAsset(ConversionAsset):
    energy_consumption_kwhpkm: float


class ElectricCoversionAsset(ConversionAsset):
    capacityElectricity_kW: float


class HeatConversionAsset(ConversionAsset):
    deliveryTemp_degc: float


class ChemicalHeatConversionAsset(HeatConversionAsset):
    capacityHeat_kW: float


class ElectricHeatConversionAsset(HeatConversionAsset):
    capacityElectricity_kW: float


class TransportHeatConversionAsset(ElectricHeatConversionAsset):
    ambientTempType: AmbientTempTypeEnum


class HybridHeatCoversionAsset(
    TransportHeatConversionAsset, ChemicalHeatConversionAsset
):
    pass
