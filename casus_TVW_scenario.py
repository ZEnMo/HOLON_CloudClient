from pathlib import Path
import numpy

from cloudclient.datamodel import Payload, Actor, Contract, defaults

# actors = [
#     Actor(
#         category="CONNECTIONOWNER",
#         type="commercial",
#         id="com1",
#         parent_actor="hol1",
#         contracts=[
#             Contract(type="DEFAULT", contract_scope="ENERGYHOLON"),
#             # Contract(
#             #     type="NONFIRMATO",
#             #     contract_scope="GRIDOPERATOR",
#             #     nfATO_capacity_kW=1750.0,
#             #     nfATO_starttime_h=16.0,
#             #     nfATO_endtime_h=8.0,
#             # ),
#             Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
#         ],
#     ),
#     Actor(
#         category="CONNECTIONOWNER",
#         type="commercial",
#         id="com5",
#         parent_actor="hol1",
#         contracts=[
#             Contract(type="DEFAULT", contract_scope="ENERGYHOLON"),
#             # Contract(
#             #     type="NONFIRMATO",
#             #     contract_scope="GRIDOPERATOR",
#             #     nfATO_capacity_kW=1750.0,
#             #     nfATO_starttime_h=16.0,
#             #     nfATO_endtime_h=8.0,
#             # ),
#             Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
#         ],
#     ),
#     Actor(
#         category="CONNECTIONOWNER",
#         type="commercial",
#         id="com2",
#         parent_actor="hol1",
#         contracts=[
#             Contract(type="DEFAULT", contract_scope="ENERGYHOLON"),
#             Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
#         ],
#     ),
#     Actor(
#         category="CONNECTIONOWNER",
#         type="commercial",
#         id="com3",
#         parent_actor="hol1",
#         contracts=[Contract(type="DEFAULT", contract_scope="ENERGYHOLON")],
#     ),
#     Actor(
#         category="CONNECTIONOWNER",
#         type="commercial",
#         id="com4",
#         parent_actor="hol1",
#         contracts=[
#             Contract(type="DEFAULT", contract_scope="ENERGYHOLON"),
#             Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
#         ],
#     ),
#     Actor(
#         category="ENERGYSUPPLIER",
#         id="sup1",
#         parent_actor="nat",
#     ),
#     Actor(
#         category="ENERGYHOLON",
#         id="hol1",
#         parent_actor="sup1",
#         contracts=[
#             Contract(type="NODALPRICING", contract_scope="GRIDOPERATOR"),
#             Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
#             Contract(
#                 type="NONFIRMATO",
#                 contract_scope="GRIDOPERATOR",
#                 nfATO_capacity_kW=5000.0,
#                 nfATO_starttime_h=16.0,
#                 nfATO_endtime_h=7.0,
#             ),
#         ],
#     ),
#     Actor(
#         category="GRIDOPERATOR",
#         id="o1",
#         parent_actor="nat",
#     ),
# ]

# from cloudclient.datamodel.defaults import (
#     Diesel_Truck,
#     EHGV,
#     Solarpanel_farm,
#     Solarpanel_building,
#     Grid_battery,
#     Industry_other_heat_demand,
#     Windmill_onshore,
#     # Building_solarpanels_10kWp,
#     Building_gas_burner,
#     Office_other_electricity,
#     House_default,
#     House_hybridheatpump,
#     Office_default, 
#     Logistics_default,
#     Gridoperator_default,
#     Energysupplier_default,
#     Energyholon_default,
#     Household_default,
#     Commercial_default
# )

from cloudclient.datamodel.defaults import *

#from cloudclient.datamodel.defaults.gridConnection_defaults import (
#     House_default,
#     Office_default,
#
#
#)

# from cloudclient.datamodel.defaults import ()

#for extensive way of defining gridConnections
from cloudclient.datamodel.gridconnections import (
     HouseGridConnection,
     IndustryGridConnection,
     BuildingGridConnection,
     ProductionGridConnection,     
)

config_gridconnection_list_basic = [
  #House_electrified(amount = 40, parent_electric="E2"),
  Store_default(amount=20, parent_electric="E2"),
  House_default(amount=20, parent_electric="E2", type=HousingTypeEnum.appartment, insulation_label= InsulationLabelEnum.d),
  
  House_default(amount=40, parent_electric="E3", type=HousingTypeEnum.semidetached, insulation_label= InsulationLabelEnum.b),
  
  House_default(amount=40, parent_electric="E4", type=HousingTypeEnum.appartment, insulation_label= InsulationLabelEnum.a),
  
  House_default(amount=40, parent_electric="E5", type=HousingTypeEnum.highrise, insulation_label= InsulationLabelEnum.c),
  
  House_default(amount=30, parent_electric="E6", type=HousingTypeEnum.terraced, insulation_label= InsulationLabelEnum.c),
  House_default(amount=10, parent_electric="E6", type=HousingTypeEnum.semidetached, insulation_label= InsulationLabelEnum.c),

  House_default(amount=40, parent_electric="E7", type=HousingTypeEnum.detached, insulation_label= InsulationLabelEnum.f),

  Industry_other_default(amount=1, parent_electric = "E8"),  ## HT heat producer, zelf ook verbruik/opwek stroom?
  ResidualHeatProducer(amount = 1, parent_heat = "H1", parent_electric = "E8", owner_actor = "sup1", type = "RESIDUALHEAT", assets=[ResidualHeat_HT(capacityHeat_kW = 3000)] ),
  Industry_other_default(amount = 1, parent_electric = "E9")  ## RWZI heat producer, zelf ook verbruik/opwek stroom?

  #House_hybridheatpump(amount = 40, parent_electric="E3"),
  #Office_default(amount = 5, parent_electric="E2"),
  #Store_default(amount = 10, parent_electric="E3"),
  #Industry_other_default(amount =1, parent_electric = "E3"),
  #Logistics_default(amount = 1, parent_electric="E3")
]

config_gridconnection_list_DH = [
  #House_electrified(amount = 40, parent_electric="E2"),
  Store_default(amount=20, parent_electric="E2"),
  House_heatnetwork_basic(amount=20, parent_heat="H1", parent_electric="E2", type=HousingTypeEnum.appartment, insulation_label= InsulationLabelEnum.d),
  
  House_heatnetwork_basic(amount=40, parent_heat="H1", parent_electric="E3", type=HousingTypeEnum.semidetached, insulation_label= InsulationLabelEnum.b),
  
  House_heatnetwork_basic(amount=40, parent_heat="H1", parent_electric="E4", type=HousingTypeEnum.appartment, insulation_label= InsulationLabelEnum.a),
  
  House_heatnetwork_basic(amount=40, parent_heat="H1", parent_electric="E5", type=HousingTypeEnum.highrise, insulation_label= InsulationLabelEnum.c),
  
  House_heatnetwork_basic(amount=30, parent_heat="H1", parent_electric="E6", type=HousingTypeEnum.terraced, insulation_label= InsulationLabelEnum.c),
  House_heatnetwork_basic(amount=10, parent_heat="H1", parent_electric="E6", type=HousingTypeEnum.semidetached, insulation_label= InsulationLabelEnum.c),

  House_heatnetwork_basic(amount=40, parent_heat="H1", parent_electric="E7", type=HousingTypeEnum.detached, insulation_label= InsulationLabelEnum.f),

  Industry_other_default(amount=1, parent_electric = "E8"),  ## HT heat producer, zelf ook verbruik/opwek stroom?
  #ResidualHeatProducer(amount = 1, parent_heat = "H1", parent_electric = "E8", owner_actor = "sup1", type = "RESIDUALHEATHT", assets=[ResidualHeat_HT(capacityHeat_kW = 600)] ),
  #ResidualHeatProducer(amount = 1, parent_heat = "H1", parent_electric = "E8", owner_actor = "sup1", type = "RESIDUALHEATLT", assets=[ResidualHeat_LT(capacityHeat_kW = 600)] ),
  #DistrictHeating_HT_Gasburner(amount = 1, heating_type = "GASFIRED_CHPPEAK", parent_heat = "H1", parent_electric = "E8", owner_actor = "sup1", assets=[DH_boiler_L, Methane_CHP_M, District_Heating_heat_buffer_HT_S]),
  #DistrictHeating_HT_Heatpump_gaspeak(amount = 1, parent_heat = "H1", parent_electric = "E8", owner_actor = "sup1" ),
  #DistrictHeating_HT_Heatpump_gaspeak(amount = 1, parent_heat = "H1", parent_electric = "E8", owner_actor = "sup1" ),
  DistrictHeating_MT_Heatpump_gaspeak(amount = 1, parent_heat = "H1", parent_electric = "E8", heating_type = "LT_RESIDUAL_HEATPUMP_GASPEAK", owner_actor = "sup1", assets=[ResidualHeat_LT(capacityHeat_kW = 600), DH_heat_pump_MT_S, District_Heating_heat_buffer_MT_S ]),

  Industry_other_default(amount = 1, parent_electric = "E9")  ## RWZI heat producer, zelf ook verbruik/opwek stroom?

  #House_hybridheatpump(amount = 40, parent_electric="E3"),
  #Office_default(amount = 5, parent_electric="E2"),
  #Store_default(amount = 10, parent_electric="E3"),
  #Industry_other_default(amount =1, parent_electric = "E3"),
  #Logistics_default(amount = 1, parent_electric="E3")
]

## select gridConnection list to use...
config_gridconnection_list = config_gridconnection_list_DH

config_actors_list = [
    Gridoperator_default(amount = 1, id="o1"),
    Energysupplier_default(amount = 1, id="sup1"),
    #Energysupplier_default(amount = 1, id="sup2"),
    #Energyholon_default(amount = 1, id="hol1", parent_actor = "sup1"),

    Household_default(amount=20+40+40+40+40+40, parent_actor = "sup1"),
    #Household_default(amount=200, parent_actor = "hol1"),
    Commercial_default(amount=20, parent_actor = "sup1"),
    #Commercial_default(amount=25, parent_actor = "hol1")
]

numpy.random.seed(0)

def stochasticValue(average: float, stdev: float) -> float:
    value = numpy.random.normal(average, stdev, 1)
    value = numpy.round(value, 3)
    return value


#print("CONFIG LIST",config_gridconnection_list)
gridconnections = []

pricelevel_low_dif_from_avg_eurpkWh_mean = 0.02
pricelevel_low_dif_from_avg_eurpkWh_stdev = 0.002
pricelevel_high_dif_from_avg_eurpkWh_mean = 0.01
pricelevel_high_dif_from_avg_eurpkWh_stdev = 0.001



for item in config_gridconnection_list:
    #object_type = key
    #data = config_list[key]
    #####print("key: ",key,"datarow: ", data)
    #print(item)
    
    for i in range(0, item.amount):
        #print(key,i)
        
        id = ""
        owneractor = ""

        #print("class naaaaaame ",item.__class__.__bases__[0].__name__)
        x_ = getattr(defaults, str(item.__class__.__bases__[0].__name__))
        category = x_.__name__
        
        print("test******************", category)
        if( category == "ProductionGridConnection"):
            gridconnections.append(x_(id=item.id, category = item.category, owner_actor=item.owner_actor, capacity_kw=item.capacity_kw, assets=item.assets, parent_electric=item.parent_electric, parent_heat=item.parent_heat))
        elif( category == "DistrictHeatingGridConnection"):
            gridconnections.append(x_(id=item.id, category = item.category, owner_actor=item.owner_actor, capacity_kw=item.capacity_kw, assets=item.assets, parent_electric=item.parent_electric, parent_heat=item.parent_heat, heating_type = item.heating_type, type=item.type))
        elif( category == "IndustryGridConnection"):
            gridconnections.append(x_(id=item.id, owner_actor=item.owner_actor, capacity_kw=item.capacity_kw, assets=item.assets, heating_type=item.heating_type, type=item.type, parent_electric=item.parent_electric))
        elif( category == "BuildingGridConnection"):
            gridconnections.append(x_(id=item.id, owner_actor=item.owner_actor, capacity_kw=item.capacity_kw, insulation_label=item.insulation_label, assets=item.assets, heating_type=item.heating_type, type=item.type, parent_electric=item.parent_electric, parent_heat=item.parent_heat, charging_mode = item.charging_mode))
        else:
            gridconnections.append(x_(id=item.id, owner_actor=item.owner_actor, capacity_kw=item.capacity_kw, insulation_label=item.insulation_label, assets=item.assets, heating_type=item.heating_type, type=item.type, parent_electric=item.parent_electric, parent_heat=item.parent_heat, charging_mode = item.charging_mode, smart_assets = item.smart_assets, pricelevel_low_dif_from_avg_eurpkWh = stochasticValue(pricelevel_low_dif_from_avg_eurpkWh_mean, pricelevel_low_dif_from_avg_eurpkWh_stdev), pricelevel_high_dif_from_avg_eurpkWh = stochasticValue(pricelevel_high_dif_from_avg_eurpkWh_mean, pricelevel_high_dif_from_avg_eurpkWh_stdev)))


## Force unique id's for gridconnections    
number_of_houses = 0
number_of_buildings = 0

for i in gridconnections:  
    #print("caaataagory ",i.category)
    #print("ifff",i.id)
    #print("owner actor", i.owner_actor)

    if i.category == "HOUSE" and i.id == "":
        number_of_houses = number_of_houses + 1
        id = "h"+str(number_of_houses)
        owner_actor = "hh"+str(number_of_houses)
        i.id = id
        if i.owner_actor == "":
            i.owner_actor = owner_actor
    elif i.category == "BUILDING" or "INDUSTRY" and i.id == "":
        number_of_buildings = number_of_buildings + 1
        id = "b"+str(number_of_buildings)
        owner_actor = "com"+str(number_of_buildings)
        i.id = id
        if i.owner_actor == "":
            i.owner_actor = owner_actor
        


    #*[Office_default] * 2
 
    # BuildingGridConnection(
    #     insulation_label="NONE",
    #     heating_type="GASBURNER",
    #     type="LOGISTICS",
    #     owner_actor="com1",
    #     parent_electric="E2",
    #     id="b1",
    #     capacity_kw=1750,
    #     charging_mode="CHEAP",
    #     battery_mode="BALANCE",
    #     assets=[
    #         *[EHGV] * 5,
    #         # Diesel_Truck,
    #         Building_gas_burner(capacityHeat_kW=200),
    #         Solarpanel_building(capacityElectricity_kW=500),
    #         Grid_battery(storageCapacity_kWh=0),
    #         # Building_solarpanels_10kWp,
    #     ],
    # ),
    # BuildingGridConnection(
    #     insulation_label="NONE",
    #     heating_type="GASBURNER",
    #     type="LOGISTICS",
    #     owner_actor="com5",
    #     parent_electric="E2",
    #     id="b5",
    #     capacity_kw=1750,
    #     charging_mode="CHEAP",
    #     battery_mode="BALANCE",
    #     assets=[
    #         *[EHGV] * 5,
    #         # Diesel_Truck,
    #         Building_gas_burner(capacityHeat_kW=200),
    #         Solarpanel_building(capacityElectricity_kW=500),
    #         Grid_battery(storageCapacity_kWh=0),
    #         # Building_solarpanels_10kWp,
    #     ],
    # ),
    # BuildingGridConnection(
    #     insulation_label="NONE",
    #     heating_type="GASBURNER",
    #     type="LOGISTICS",
    #     owner_actor="com5",
    #     parent_electric="E2",
    #     id="b6",
    #     capacity_kw=1750,
    #     charging_mode="CHEAP",
    #     battery_mode="BALANCE",
    #     assets=[
    #         *[EHGV] * 5,
    #         # Diesel_Truck,
    #         Building_gas_burner(capacityHeat_kW=200),
    #         Solarpanel_building(capacityElectricity_kW=500),
    #         Grid_battery(storageCapacity_kWh=0),
    #         # Building_solarpanels_10kWp,
    #     ],
    # ),
    # IndustryGridConnection(
    #     heating_type="GASBURNER",
    #     type="INDUSTRY_OTHER",
    #     owner_actor="com2",
    #     parent_electric="E2",
    #     id="b2",
    #     capacity_kw=3000,
    #     assets=[
    #         Industry_other_heat_demand,
    #         Building_gas_burner(capacityHeat_kW=100),
    #         Office_other_electricity,
    #     ],
    # ),
    # ProductionGridConnection(
    #     category="WINDFARM",
    #     owner_actor="com3",
    #     parent_electric="E2",
    #     id="b3",
    #     capacity_kw=8000,
    #     assets=[
    #         Windmill_onshore(capacityElectricity_kW=6000),
    #         Solarpanel_farm(capacityElectricity_kW=2000),
    #     ],
    # ),
    # # ProductionGridConnection(
    # #     category="SOLARFARM",
    # #     owner_actor="com3",
    # #     parent_electric="E2",
    # #     id="b3",
    # #     capacity_kw=7000,
    # #     assets=[Solarpanel_farm(capacityElectricity_kW=2000)],
    # # ),
    # ProductionGridConnection(
    #     category="GRIDBATTERY",
    #     owner_actor="com4",
    #     parent_electric="E2",
    #     battery_mode="PRICE",
    #     id="b4",
    #     capacity_kw=8000,
    #     assets=[
    #         Grid_battery(
    #             storageCapacity_kWh=30000,
    #             capacityElectricity_kW=10000,
    #             stateOfCharge_r=0.2,
    #         )
    #     ],
    # ),
#]

## actors generated new style: ##

from cloudclient.datamodel.defaults import (
    actors_defaults
)

from cloudclient.datamodel.actors import *
actors = []

for item in config_actors_list:
    #object_type = key
    #data = config_list[key]
    #####print("key: ",key,"datarow: ", data)
    #print(item)
    for i in range(0, item.amount):
        #print(key,i)
        
        #print("class naaaaaame ",item.__class__.__bases__[0].__name__)
        x_ = getattr(defaults, str(item.__class__.__bases__[0].__name__))
        category = x_.__name__
        
        actors.append(x_(category = item.category, type = item.type, id = item.id, parent_actor = item.parent_actor, contracts = item.contracts))

number_of_households = 0
number_of_commercials = 0

for i in actors:
    #print("caaataagory ",i.category)
    #print("ifff",i.id)
    if i.category == ActorTypeEnum.connectionowner and i.type == None:
        number_of_households = number_of_households + 1
        id = "hh"+str(number_of_households)
        #owner_actor = "a"+str(number_of_households)
        i.id = id
    elif i.category == ActorTypeEnum.connectionowner and i.type == SubTypeEnum.commercial:
        number_of_commercials = number_of_commercials + 1
        id = "com"+str(number_of_commercials)
        #owner_actor = "com"+str(number_of_commercials)
        i.id = id
    elif i.id == None:
        id = "extra"
        owner_actor = "extra"
        i.id = id
    
    #i.owner_actor = owner_actor

#print(actors)


## gridnodes
from cloudclient.datamodel.gridnodes import ElectricGridNode, HeatGridNode

gridnodes = [
    ElectricGridNode(
        id="E2",
        parent="E1",
        owner_actor="o1",
        capacity_kw=5000,
        category="ELECTRICITY",
        type="MSLS",
    ),
    ElectricGridNode(
        id="E3",
        parent="E1",
        owner_actor="o1",
        capacity_kw=5000,
        category="ELECTRICITY",
        type="MSLS",
    ),
    ElectricGridNode(
        id="E4",
        parent="E1",
        owner_actor="o1",
        capacity_kw=5000,
        category="ELECTRICITY",
        type="MSLS",
    ),
    ElectricGridNode(
        id="E5",
        parent="E1",
        owner_actor="o1",
        capacity_kw=5000,
        category="ELECTRICITY",
        type="MSLS",
    ),
    ElectricGridNode(
        id="E6",
        parent="E1",
        owner_actor="o1",
        capacity_kw=5000,
        category="ELECTRICITY",
        type="MSLS",
    ),
    ElectricGridNode(
        id="E7",
        parent="E1",
        owner_actor="o1",
        capacity_kw=5000,
        category="ELECTRICITY",
        type="MSLS",
    ),
    ElectricGridNode(
        id="E8",
        parent="E1",
        owner_actor="o1",
        capacity_kw=5000,
        category="ELECTRICITY",
        type="MSLS",
    ),    
    ElectricGridNode(
        id="E9",
        parent="E1",
        owner_actor="o1",
        capacity_kw=5000,
        category="ELECTRICITY",
        type="MSLS",
    ),
    ElectricGridNode(
        id="E1",
        owner_actor="o1",
        capacity_kw=500000,
        category="ELECTRICITY",
        type="HSMS",
    ),
    HeatGridNode(
        id="H1",
        owner_actor="o1",
        capacity_kw=500000,
        category="HEAT",
        type="LT",
        assets=[District_Heating_network_LT_L],
    ),
]

from cloudclient.datamodel.policies import Policy

policies = [
    # Policy(
    #     parameter="EV_charging_attitude_standard",
    #     value="CHEAP",
    #     unit=None,
    #     comment="charging behaviour not contingent on holon",
    # ),
    Policy(
        parameter="Grid_MS_congestion_allowance_level_kW",
        value="0",
        unit="kW",
        comment="gridOperator policy variable",
    ),
    Policy(
        parameter="Grid_MS_congestion_price_eurpkWh",
        value="0.2",
        unit="eurpkWh",
        comment="gridOperator policy value",
    ),
    Policy(
        parameter="Grid_MS_congestion_threshold_fr",
        value="0.5",
        unit="fr",
        comment="gridOperator policy value",
    ),
    Policy(
        parameter="Grid_MS_congestion_pricing_consumption_eurpkWh",
        value="TRUE",
        unit=None,
        comment="gridOperator policy value",
    ),
    Policy(
        parameter="Grid_MS_congestion_pricing_production_eurpkWh",
        value="TRUE",
        unit=None,
        comment="gridOperator policy value",
    ),
    Policy(
        parameter="Fixed_electricity_price_eurpkWh",
        value="0.21",
        unit="EUR p kWh",
        comment="Fixed_electricity_price",
    ),
    Policy(
        parameter="Fixed_heat_price_eurpkWh",
        value="0.10",
        unit="EUR p kWh",
        comment="Fixed_heat_price",
    ),
    Policy(
        parameter="Fixed_methane_price_eurpkWh",
        value="0.05",
        unit="EUR p kWh",
        comment="Fixed_methane_price",
    ),
    Policy(
        parameter="Fixed_hydrogen_price_eurpkWh",
        value="0.3",
        unit="EUR p kWh",
        comment="Fixed_hydrogen_price",
    ),
    Policy(
        parameter="Energy_supplier_electricity_price_margin_eurpkWh",
        value="0.17",
        unit="fr",
        comment="p_variableElectricityPriceOverNational_eurpkWh",
    ),
    Policy(
        parameter="Fixed_electricity_feed_in_tariff_eurpkWh",
        value="0.1",
        unit="EUR_pKWh",
        comment="p_fixedFeedinTariff_eurpkWh",
    ),
    Policy(
        parameter="Fixed_diesel_price_eurpkWh",
        value="0.2",
        unit="EUR_pKWh",
        comment="Fixed_diesel_price",
    ),
    Policy(
        parameter="Time_buffer_for_spread_charging_min",
        value="60",
        unit="minutes",
        comment="Time_buffer_for_spread_charging, Integer value",
    ),
    Policy(
        parameter="Salderen",
        value="false",
        unit="boolean",
        comment="switch for salderen",
    ),
    Policy(
        parameter="Capacitypricing_households_kW",
        value="5",
        unit="int",
        comment="power level at which capacity pricing kicks in",
    ),
    Policy(
        parameter="Capacitypricing_households_eur",
        value="0.5",
        unit="float",
        comment="capacity price value for households",
    ),
]

etm_slider_settings = {
    "share_of_electric_trucks": 50,
    "installed_energy_grid_battery": 0,
}

curve_mapping_for_upscaling = {
    "totalEHGVHourlyChargingProfile_kWh": "totalEHGVHourlyChargingProfile_kWh",
    "totalGridBatteryHourlyChargingProfile_kWh": "totalBatteryHourlyChargingProfile_kWh",
}

payload = Payload(
    actors=actors,
    gridconnections=gridconnections,
    gridnodes=gridnodes,
    policies=policies,
    etm_upscale_sliders=etm_slider_settings,
    etm_upscale_curve_labels=curve_mapping_for_upscaling,
)
import json

base_path = Path(__file__).parent / "doc" / "assets"

for key, json_output in payload.to_json().items():
    variable_filename = f"example_{key}.json"
    fp = base_path / variable_filename
    with open(fp, "w") as outfile:
        json.dump(json_output, outfile, indent=2)

with open(base_path / "example_total.json", "w") as outfile:
    json.dump(json.loads(payload.json()), outfile, indent=2)
