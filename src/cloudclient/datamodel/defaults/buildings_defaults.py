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
    Building_heatpump_20kW,
    Building_DH_heatdeliveryset_MT,
    Building_DH_heatdeliveryset_HT,
    Office_other_electricity,
    Store_other_electricity,
    Store_heat_demand,
    Office_heat_demand
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
    assets = [Office_other_electricity(), Building_gas_burner(capacityHeat_kW= 60.0)]

class Store_default(BuildingGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.gasburner
    type = BuildingTypeEnum.store
    assets = [Store_other_electricity(), Building_gas_burner(capacityHeat_kW= 60.0)]

class Store_heatpump(BuildingGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.heatpump_air
    type = BuildingTypeEnum.store
    assets = [
        Store_other_electricity(), 
        Building_heatpump_20kW,
        Solarpanel_building(capacityElectricity_kW=3),
    ]

class Store_hybridheatpump(BuildingGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.heatpump_gaspeak
    type = BuildingTypeEnum.store
    assets = [
        Store_other_electricity(), 
        Building_heatpump_20kW,
        Building_gas_burner(),
        Solarpanel_building(capacityElectricity_kW=3),
    ]

class Store_heatnetwork(BuildingGridConnection):   # space heating from district heating network. No hot water demand assumed! = no assets for decentral boosting.
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.districtheat
    type = BuildingTypeEnum.store
    assets = [
        Store_other_electricity(), 
        Building_DH_heatdeliveryset_HT,
        Solarpanel_building(capacityElectricity_kW=3)
    ]


class Store_heatnetwork_MT(BuildingGridConnection):   # space heating from district heating network. No hot water demand assumed! = no assets for decentral boosting.
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.districtheatDecentral
    type = BuildingTypeEnum.store
    assets = [
        Store_other_electricity(), 
        Building_DH_heatdeliveryset_MT,
        Solarpanel_building(capacityElectricity_kW=3)
]




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

