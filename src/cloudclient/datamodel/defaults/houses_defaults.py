
from cloudclient.datamodel.gridconnections import *

from cloudclient.datamodel.gridconnections import (
     HouseGridConnection,
     IndustryGridConnection,
     BuildingGridConnection,
     ProductionGridConnection,
)

from cloudclient.datamodel.defaults import *
# from cloudclient.datamodel.defaults import (
#     Diesel_Truck,
#     EHGV,
#     Solarpanel_farm,
#     Solarpanel_building,
#     Grid_battery,
#     Industry_other_heat_demand,
#     House_gas_burner,
#     House_heatpump_MT_M,
#     House_hot_water
#     Windmill_onshore,
#     # Building_solarpanels_10kWp,
#     Building_gas_burner,
#     Office_other_electricity    
# )


class House_default(HouseGridConnection):
    amount: Optional[int]
    owner_actor="" 
    id=""
    capacity_kw = 17.0
    parent_electric = ""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.gasburner
    charging_mode = ChargingModeEnum.simple
    smart_assets = SmartAssetsEnum.false
    pricelevel_low_dif_from_avg_eurpkWh = 0.02
    pricelevel_high_dif_from_avg_eurpkWh = 0.01
    assets = [
        House_other_electricity,
        House_hot_water,
        House_gas_burner(capacityHeat_kW=30),
        Diesel_Vehicle,
        #Solarpanel_building(capacityElectricity_kW=3),
    ]
    type = HousingTypeEnum.semidetached

class House_electrified(HouseGridConnection):
    amount: Optional[int]
    owner_actor="" 
    id=""
    capacity_kw = 17.0
    parent_electric = ""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.heatpump_air
    charging_mode = ChargingModeEnum.cheap
    smart_assets = SmartAssetsEnum.true
    price_level_low_dif_from_avg_eurpkWh = 0.02
    price_level_high_dif_from_avg_eurpkWh = 0.01
    assets = [
        House_other_electricity,
        House_hot_water,
        Electric_hob,
        House_heatpump_MT_M,
        House_heat_buffer,
        Solarpanel_building(capacityElectricity_kW=3),
        EV,
    ]
    type = HousingTypeEnum.semidetached

class House_electrified_dieselcar(HouseGridConnection):
    amount: Optional[int]
    owner_actor="" 
    id=""
    capacity_kw = 17.0
    parent_electric = ""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.heatpump_air
    charging_mode = ChargingModeEnum.cheap
    smart_assets = SmartAssetsEnum.true
    price_level_low_dif_from_avg_eurpkWh = 0.02
    price_level_high_dif_from_avg_eurpkWh = 0.01
    assets = [
        House_other_electricity,
        House_hot_water,
        Electric_hob,
        House_heatpump_MT_M,
        House_heat_buffer,
        Solarpanel_building(capacityElectricity_kW=3),
        #EV,
        Diesel_Vehicle,
    ]
    type = HousingTypeEnum.semidetached

class House_hybridheatpump(HouseGridConnection):
    amount: Optional[int]
    owner_actor="" 
    id=""
    capacity_kw = 17.0
    parent_electric = ""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.heatpump_gaspeak
    charging_mode = ChargingModeEnum.cheap
    smart_assets = SmartAssetsEnum.true
    price_level_low_dif_from_avg_eurpkWh = 0.02
    price_level_high_dif_from_avg_eurpkWh = 0.01
    assets = [
        House_other_electricity,
        House_hot_water,
        House_heatpump_MT_M,
        House_gas_burner(capacityHeat_kW=30),
        Solarpanel_building(capacityElectricity_kW=3),
        EV,
    ]
    type = HousingTypeEnum.semidetached

class House_heatnetwork_basic(HouseGridConnection):
    amount: Optional[int]
    owner_actor=""
    id=""
    capacity_kw = 17.0
    parent_electric = ""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.districtheat
    charging_mode = ChargingModeEnum.cheap
    smart_assets = SmartAssetsEnum.false
    price_level_low_dif_from_avg_eurpkWh = 0.02
    price_level_high_dif_from_avg_eurpkWh = 0.01
    assets = [
        House_other_electricity,
        House_hot_water,
        House_DH_heatdeliveryset,
        Solarpanel_building(capacityElectricity_kW=3),
        Diesel_Vehicle,
    ]
    type = HousingTypeEnum.semidetached


# House_default_1 = HouseGridConnection( 
#     owner_actor = "",
#     id="",
#     capacity_kw = 17.0,
#     parent_electric = "",
#     insulation_label = "C",
#     heating_type="GASBURNER",
#     type = "DETACHED",
#     assets = [
#         House_gas_burner(),
#         Solarpanel_building()
#     ],
# )