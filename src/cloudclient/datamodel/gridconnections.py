from pydantic import BaseModel, Extra
from typing import Optional, List
from cloudclient.datamodel.assets import EnergyAsset

from enum import Enum


class GridCategoryEnum(Enum):
    building = "BUILDING"
    industry = "INDUSTRY"


class ChargingModeEnum(Enum):
    max_power = "MAX_POWER"
    max_spread = "MAX_SPREAD"
    cheap = "CHEAP"
    simple = "SIMPLE"


class BatteryModeEnum(Enum):
    balance = "BALANCE"
    price = "PRICE"


class ElectrolyserModeEnum(Enum):
    balance = "BALANCE"
    price = "PRICE"
    target = "TARGET"


class GridConnection(BaseModel, extra=Extra.forbid):
    owner_actor: str
    id: str
    capacity_kw: float
    parent_electric: str
    parent_heat: Optional[str]
    assets = []
    category = "GENERIC"
    # TODO: Technical debt to match AnyLogic
    charging_mode: Optional[ChargingModeEnum]
    battery_mode: Optional[BatteryModeEnum]
    electrolyser_mode: Optional[ElectrolyserModeEnum]


class InsulationLabelEnum(Enum):
    a = "A"
    b = "B"
    c = "C"
    d = "D"
    e = "E"
    f = "F"
    g = "G"
    none = "NONE"


class HeatingTypeEnum(Enum):
    gasburner = "GASBURNER"
    gasfired = "GASFIRED"
    heatpump_gaspeak = "HEATPUMP_GASPEAK"
    districtheat = "DISTRICTHEAT"
    heatpump_boilerpeak = "HEATPUMP_BOILERPEAK"
    heatpump_air = "HEATPUMP_AIR"
    hydrogenfired = "HYDROGENFIRED"
    gasfired_CHPpeak = "GASFIRED_CHPPEAK"
    lt_residual_heatpump_gaspeak = "LT_RESIDUAL_HEATPUMP_GASPEAK"
    none = "NONE"


class ChargingModeEnum(Enum):
    simple = "SIMPLE"
    cheap = "CHEAP"


class SmartAssetsEnum(Enum):
    true = "TRUE"
    false = "FALSE"


class BuiltEnvironmentGridConnection(GridConnection):
    category = "BUILT_ENVIRONMENT"
    insulation_label: InsulationLabelEnum
    heating_type: HeatingTypeEnum


class UtilityGridConnection(GridConnection):
    category = "UTILITY"
    heating_type: HeatingTypeEnum
    assets = []


class HousingTypeEnum(Enum):
    semidetached = "SEMIDETACHED"
    terraced = "TERRACED"
    detached = "DETACHED"
    appartment = "APPARTMENT"
    highrise = "HIGHRISE"


class HouseGridConnection(BuiltEnvironmentGridConnection):
    category = "HOUSE"
    type: HousingTypeEnum
    charging_mode: ChargingModeEnum
    smart_assets = SmartAssetsEnum.false
    pricelevel_low_dif_from_avg_eurpkWh = 0.02
    pricelevel_high_dif_from_avg_eurpkWh = 0.01


class BuildingTypeEnum(Enum):
    store = "STORE"
    office = "OFFICE"
    logistics = "LOGISTICS"


class BuildingGridConnection(BuiltEnvironmentGridConnection):
    category = "BUILDING"
    type: BuildingTypeEnum


class ProductionCategoryEnum(Enum):
    windfarm = "WINDFARM"
    solarfarm = "SOLARFARM"
    gridbattery = "GRIDBATTERY"
    residualheat = "RESIDUALHEAT"


class ProductionGridConnection(GridConnection):
    category: ProductionCategoryEnum


class IndustryTypeEnum(Enum):
    steel = "STEEL"
    industry_other = "INDUSTRY_OTHER"


class IndustryGridConnection(UtilityGridConnection):
    category = "INDUSTRY"
    type: IndustryTypeEnum


class DistrictHeatingTypeEnum(Enum):
    mt = "MT"
    ht = "HT"


class DistrictHeatingGridConnection(UtilityGridConnection):
    category = "DISTRICTHEATING"
    type: DistrictHeatingTypeEnum
