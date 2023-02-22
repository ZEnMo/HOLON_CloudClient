from cloudclient.datamodel.defaults import (
    DistrictHeatingGridConnection
)

from cloudclient.datamodel.gridconnections import *
from cloudclient.datamodel.defaults import *

class DistrictHeating_HT_Gasburner(DistrictHeatingGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    heating_type = HeatingTypeEnum.gasfired
    type = DistrictHeatingTypeEnum.ht
    assets = [DH_boiler_L, DH_boiler_L, District_Heating_heat_buffer_HT_S]

class DistrictHeating_HT_Heatpump_gaspeak(DistrictHeatingGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    heating_type = HeatingTypeEnum.heatpump_gaspeak
    type = DistrictHeatingTypeEnum.ht
    assets = [DH_heat_pump_HT_S, DH_boiler_L, District_Heating_heat_buffer_HT_S]

class DistrictHeating_MT_Heatpump_gaspeak(DistrictHeatingGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 30.0
    parent_electric=""
    heating_type = HeatingTypeEnum.heatpump_gaspeak
    type = DistrictHeatingTypeEnum.mt
    assets = [DH_heat_pump_MT_S, DH_boiler_L, District_Heating_heat_buffer_MT_S]

