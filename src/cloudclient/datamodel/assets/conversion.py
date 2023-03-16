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
    heat_pump_water = "HEAT_PUMP_WATER"
    hydrogen_furnace = "HYDROGEN_FURNACE"
    methane_furnace = "METHANE_FURNACE"
    diesel_vehicle = "DIESEL_VEHICLE"
    curtailer = "CURTAILER"
    curtailer_heat = "CURTAILER_HEAT"
    methane_chp = "METHANE_CHP"
    electric_hob = "ELECTRIC_HOB"
    gas_pit = "GAS_PIT"


class ConversionAsset(EnergyAsset):
    category = "CONVERSION"
    type: ConversionAssetTypeEnum
    eta_r: float
    name: str


class VehicleConversionAsset(ConversionAsset):
    energyConsumption_kWhpkm: float
    vehicleScaling: int


class ElectricCoversionAsset(ConversionAsset):
    capacityElectricity_kW: float


class HeatConversionAsset(ConversionAsset):
    deliveryTemp_degC: Optional[float]


class ChemicalHeatConversionAsset(HeatConversionAsset):
    capacityHeat_kW: float


class ElectricHeatConversionAsset(HeatConversionAsset):
    capacityElectricity_kW: float

class TransportHeatConversionAsset(ElectricHeatConversionAsset):
    ambientTempType: Optional[AmbientTempTypeEnum]


class CombinedHeatPowerAsset(ElectricHeatConversionAsset, ChemicalHeatConversionAsset):

    pass

class HybridHeatCoversionAsset(
    TransportHeatConversionAsset, ChemicalHeatConversionAsset
):
    pass

