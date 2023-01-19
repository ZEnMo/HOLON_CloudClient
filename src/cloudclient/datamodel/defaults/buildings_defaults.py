from cloudclient.datamodel.defaults import (
    Diesel_Truck,
    EHGV,
    Solarpanel_farm,
    Solarpanel_building,
    Grid_battery,
    Industry_other_heat_demand,
    Windmill_onshore,
    # Building_solarpanels_10kWp,
    Building_gas_burner,
    Office_other_electricity
)

from cloudclient.datamodel.gridconnections import *

class Office_default(BuildingGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.gasburner
    type = BuildingTypeEnum.office
    assets = [Building_gas_burner(capacityHeat_kW= 200.0)]

class Store_default(BuildingGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.gasburner
    type = BuildingTypeEnum.store
    assets = [Solarpanel_building(capacityElectricity_kW = 100)]

class Logistics_default(BuildingGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.gasburner
    type = BuildingTypeEnum.logistics
    assets = [*[EHGV]*5, Solarpanel_building(capacityElectricity_kW = 100)]

