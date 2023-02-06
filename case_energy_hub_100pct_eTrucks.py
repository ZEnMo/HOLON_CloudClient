from pathlib import Path

from cloudclient.datamodel import Payload, Actor, Contract

actors = [
    Actor(
        category="CONNECTIONOWNER",
        type="commercial",
        id="com1",
        parent_actor="hol1",
        contracts=[
            # Contract(type="DEFAULT", contract_scope="ENERGYHOLON"),
            # Contract(
            #     type="NONFIRMATO",
            #     contract_scope="GRIDOPERATOR",
            #     nfATO_capacity_kW=1000.0,
            #     nfATO_starttime_h=20.0,
            #     nfATO_endtime_h=8.0,
            # ),
            Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
        ],
    ),
    Actor(
        category="CONNECTIONOWNER",
        type="commercial",
        id="com5",
        parent_actor="hol1",
        contracts=[
            # Contract(type="DEFAULT", contract_scope="ENERGYHOLON"),
            # Contract(
            #     type="NONFIRMATO",
            #     contract_scope="GRIDOPERATOR",
            #     nfATO_capacity_kW=1000.0,
            #     nfATO_starttime_h=20.0,
            #     nfATO_endtime_h=8.0,
            # ),
            Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
        ],
    ),
    Actor(
        category="CONNECTIONOWNER",
        type="commercial",
        id="com2",
        parent_actor="hol1",
        contracts=[
            Contract(type="DEFAULT", contract_scope="ENERGYHOLON"),
            # Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
        ],
    ),
    Actor(
        category="CONNECTIONOWNER",
        type="commercial",
        id="com3",
        parent_actor="hol1",
        contracts=[Contract(type="DEFAULT", contract_scope="ENERGYHOLON")],
    ),
    Actor(
        category="CONNECTIONOWNER",
        type="commercial",
        id="com4",
        parent_actor="hol1",
        contracts=[
            Contract(type="DEFAULT", contract_scope="ENERGYHOLON"),
            # Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
        ],
    ),
    Actor(
        category="ENERGYSUPPLIER",
        id="sup1",
        parent_actor="nat",
    ),
    Actor(
        category="ENERGYHOLON",
        id="hol1",
        parent_actor="sup1",
        contracts=[
            Contract(type="NODALPRICING", contract_scope="GRIDOPERATOR"),
            Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
            Contract(
                type="NONFIRMATO",
                contract_scope="GRIDOPERATOR",
                nfATO_capacity_kW=5000.0,
                nfATO_starttime_h=20.0,
                nfATO_endtime_h=7.0,
            ),
        ],
    ),
    Actor(
        category="GRIDOPERATOR",
        id="o1",
        parent_actor="nat",
    ),
]

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
    Office_other_electricity,
)

# from cloudclient.datamodel.defaults import *

from cloudclient.datamodel.gridconnections import (
    IndustryGridConnection,
    BuildingGridConnection,
    ProductionGridConnection,
)

eTrucksPerGridConnection = 5

gridconnections = [
    BuildingGridConnection(
        insulation_label="NONE",
        heating_type="GASBURNER",
        type="LOGISTICS",
        owner_actor="com1",
        parent_electric="E2",
        id="b1",
        capacity_kw=1300,
        charging_mode="MAX_POWER",
        # battery_mode="BALANCE",
        assets=[
            *[EHGV] * eTrucksPerGridConnection,
            *[Diesel_Truck] * (10 - eTrucksPerGridConnection),
            Building_gas_burner(capacityHeat_kW=200),
            # Solarpanel_building(capacityElectricity_kW=500),
            # Grid_battery(storageCapacity_kWh=0),
            # Building_solarpanels_10kWp,
        ],
    ),
    BuildingGridConnection(
        insulation_label="NONE",
        heating_type="GASBURNER",
        type="LOGISTICS",
        owner_actor="com5",
        parent_electric="E2",
        id="b5",
        capacity_kw=1300,
        charging_mode="MAX_POWER",
        # battery_mode="BALANCE",
        assets=[
            *[EHGV] * eTrucksPerGridConnection,
            *[Diesel_Truck] * (10 - eTrucksPerGridConnection),
            Building_gas_burner(capacityHeat_kW=200),
            # Solarpanel_building(capacityElectricity_kW=500),
            # Grid_battery(storageCapacity_kWh=0),
            # Building_solarpanels_10kWp,
        ],
    ),
    # BuildingGridConnection(
    #     insulation_label="NONE",
    #     heating_type="GASBURNER",
    #     type="LOGISTICS",
    #     owner_actor="com5",
    #     parent_electric="E2",
    #     id="b6",
    #     capacity_kw=1000,
    #     charging_mode="MAX_POWER",
    #     # battery_mode="BALANCE",
    #     assets=[
    #         *[EHGV] * eTrucksPerGridConnection,
    #         *[Diesel_Truck] * (5 - eTrucksPerGridConnection),
    #         Building_gas_burner(capacityHeat_kW=200),
    #         # Solarpanel_building(capacityElectricity_kW=500),
    #         # Grid_battery(storageCapacity_kWh=0),
    #         # Building_solarpanels_10kWp,
    #     ],
    # ),
    IndustryGridConnection(
        heating_type="GASBURNER",
        type="INDUSTRY_OTHER",
        owner_actor="com2",
        parent_electric="E2",
        id="b2",
        capacity_kw=3000,
        assets=[
            Industry_other_heat_demand,
            Building_gas_burner(capacityHeat_kW=100),
            Office_other_electricity,
        ],
    ),
    ProductionGridConnection(
        category="WINDFARM",
        owner_actor="com3",
        parent_electric="E2",
        id="b3",
        capacity_kw=8000,
        assets=[
            # Windmill_onshore(capacityElectricity_kW=6000),
            # Solarpanel_farm(capacityElectricity_kW=2000),
        ],
    ),
    # ProductionGridConnection(
    #     category="SOLARFARM",
    #     owner_actor="com3",
    #     parent_electric="E2",
    #     id="b3",
    #     capacity_kw=7000,
    #     assets=[Solarpanel_farm(capacityElectricity_kW=2000)],
    # ),
    ProductionGridConnection(
        category="GRIDBATTERY",
        owner_actor="com4",
        parent_electric="E2",
        battery_mode="BALANCE",
        id="b4",
        capacity_kw=8000,
        assets=[
            Grid_battery(
                storageCapacity_kWh=0 * 30000,
                capacityElectricity_kW=10000,
                stateOfCharge_r=0.2,
            )
        ],
    ),
]

from cloudclient.datamodel.gridnodes import ElectricGridNode

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
        id="E1",
        owner_actor="o1",
        capacity_kw=500000,
        category="ELECTRICITY",
        type="HSMS",
    ),
]

from cloudclient.datamodel.policies import Policy

policies = [
    # Policy(
    #     parameter="EV_charging_attitude_standard",
    #     value="MAX_POWER",
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
]

etm_upscale_slider_settings = {
    "share_of_electric_trucks": 100,  # Impacts costs, HV netload, sustainability and selfsufficiency
    "installed_energy_grid_battery": 0,
    "share_of_buildings_with_solar_panels": 0,
    # "fooled_you": -100,  # so you can just add any silly etm_key, it will just be ignored...
}


curve_mapping_for_upscaling = {
    "totalEHGVHourlyChargingProfile_kWh": "totalEHGVHourlyChargingProfile_kWh",
    "totalGridBatteryHourlyChargingProfile_kWh": "totalBatteryHourlyChargingProfile_kWh",
    # "haha": "totalBatteryHourlyChargingProfile_kWh", # so you can just add any silly etm_key, it will just be ignored...
}

payload = Payload(
    actors=actors,
    gridconnections=gridconnections,
    gridnodes=gridnodes,
    policies=policies,
    etm_upscale_sliders=etm_upscale_slider_settings,
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
