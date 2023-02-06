from cloudclient.datamodel import HeatConsumptionAsset, ElectricConsumptionAsset

Industry_steel_electricity = ElectricConsumptionAsset(
    name="Industry_steel_electricity",
    type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=1000000,
)
Industry_other_electricity = ElectricConsumptionAsset(
    name="Industry_other_electricity",
    type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=1000000,
)
Logistics_fleet_hgv_E = ElectricConsumptionAsset(
    name="Logistics_fleet_hgv_E",
    type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=6500000,
)
Industry_steel_heat = HeatConsumptionAsset(
    name="Industry_steel_heat",
    type="HEAT_DEMAND",
    yearlyDemandHeat_kWh=1000000,
)
Industry_other_heat_demand = HeatConsumptionAsset(
    name="INDUSTRY_OTHER_HEAT_DEMAND",
    type="HEAT_DEMAND",
    yearlyDemandHeat_kWh=600000.0,
)
House_hot_water = HeatConsumptionAsset(
    name="House_hot_water",
    type="HOT_WATER_CONSUMPTION",
    yearlyDemandHeat_kWh=30,
)
House_other_electricity = ElectricConsumptionAsset(
    name="House_other_electricity",
    type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=2479,
)
Office_other_electricity = ElectricConsumptionAsset(
    name="Office_other_electricity",
    type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=10000000.0,
)
Store_other_electricity = ElectricConsumptionAsset(
    name="Store_other_electricity",
    type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=35000,
)
