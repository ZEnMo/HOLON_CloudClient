from pydantic import BaseModel, Extra
from typing import Optional, List
from cloudclient.datamodel.assets import EnergyAsset

from enum import Enum


class GridCategoryEnum(Enum):
    building = "BUILDING"
    industry = "INDUSTRY"


class GridConnection(BaseModel, extra=Extra.forbid):
    owner_actor: str
    id: str
    capacity_kw: float
    parent_electric: str
    parent_heat: Optional[str]
    assets: Optional[List[EnergyAsset]]
    category = "GENERIC"


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
    hydrogenfired = "HYDROGENFIRED"
    none = "NONE"


class BuiltEnvironmentGridConnection(GridConnection):
    category = "BUILT_ENVIRONMENT"
    insulation_label: InsulationLabelEnum
    heating_type: HeatingTypeEnum


class UtilityGridConnection(GridConnection):
    category = "UTILITY"
    heating_type: HeatingTypeEnum


class HousingTypeEnum(Enum):
    semidetached = "SEMIDETACHED"
    terraced = "TERRACED"
    detached = "DETACHED"


class HouseGridConnection(BuiltEnvironmentGridConnection):
    category = "HOUSE"
    type: HousingTypeEnum


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
    category = "DISTRICT_HEATING"
    type: DistrictHeatingTypeEnum
