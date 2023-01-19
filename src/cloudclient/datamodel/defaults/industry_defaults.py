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

class Industry_other_default(IndustryGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 1000.0
    parent_electric = ""
    parent_heat = ""
    heating_type = HeatingTypeEnum.gasburner
    type = IndustryTypeEnum.industry_other
    assets = [Industry_other_heat_demand, Office_other_electricity(yearlyDemandElectricity_kWh = 3500000.0), Building_gas_burner(capacityHeat_kW = 190)] 

  