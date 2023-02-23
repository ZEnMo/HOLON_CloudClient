from enum import Enum
from cloudclient.datamodel.assets.energy import EnergyAsset, AmbientTempTypeEnum
from typing import Optional


class ConversionAssetTypeEnum(Enum):
    electric_heater = "BOILER"
    electrolyser = "ELECTROLYSER"
    gas_burner = "GAS_BURNER"
    heat_delivery_set = "HEAT_DELIVERY_SET"
    heat_pump_air = "HEAT_PUMP_AIR"
    heat_pump_ground = "HEAT_PUMP_GROUND"
    heat_pump_water = "HEAT_PUMP_WATER"
    hydrogen_furnace = "HYDROGEN_FURNACE"
    methane_furnace = "METHANE_FURNACE"
    # diesel_vehicle = "DIESEL_VEHICLE"
    curtailer = "CURTAILER"
    methane_chp = "METHANE_CHP"


class ConversionAsset(EnergyAsset):
    category = "CONVERSION"
    type: ConversionAssetTypeEnum
    eta_r: float
    name: str


class ElectricConversionAsset(ConversionAsset):
    capacityElectric_kW: float


class ChemicalConversionAsset(ConversionAsset):
    capacityMethane_kW: float


class HeatConversionAsset(ConversionAsset):
    deliveryTemp_degC: float


class ChemicalHeatConversionAsset(HeatConversionAsset):
    capacityHeat_kW: float


class ElectricHeatConversionAsset(HeatConversionAsset):
    capacityElectricity_kW: float


class TransportHeatConversionAsset(ElectricHeatConversionAsset):
    ambientTempType: Optional[AmbientTempTypeEnum]


class HybridHeatCoversionAsset(
    TransportHeatConversionAsset, ChemicalHeatConversionAsset
):
    pass
