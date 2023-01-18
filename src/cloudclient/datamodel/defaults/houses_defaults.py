
from cloudclient.datamodel.gridconnections import *

from cloudclient.datamodel.gridconnections import (
     HouseGridConnection,
     IndustryGridConnection,
     BuildingGridConnection,
     ProductionGridConnection,
)

from cloudclient.datamodel.defaults import (
    Diesel_Truck,
    EHGV,
    Solarpanel_farm,
    Solarpanel_building,
    Grid_battery,
    Industry_other_heat_demand,
    House_gas_burner,
    Windmill_onshore,
    # Building_solarpanels_10kWp,
    Building_gas_burner,
    Office_other_electricity    
)


class House_default(HouseGridConnection):
    amount: Optional[int]
    owner_actor="" 
    id=""
    capacity_kw = 17.0
    parent_electric = ""
    insulation_label = InsulationLabelEnum.c
    heating_type = HeatingTypeEnum.gasburner
    assets = [
        House_gas_burner(capacityHeat_kW=30),
        Solarpanel_building(capacityElectricity_kW=100),
    ]
    type = HousingTypeEnum.detached
    

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