from cloudclient.datamodel import (
    HeatConsumptionAsset,
    ElectricConsumptionAsset,
)
from cloudclient.datamodel.assets.consumption import *

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


class Industry_other_heat_demand(HeatConsumptionAsset):
    name = "INDUSTRY_OTHER_HEAT_DEMAND"
    type = ConsumptionAssetTypeEnum.heat_demand
    yearlyDemandHeat_kWh = 600000.0


House_hot_water = HeatConsumptionAsset(
    name="House_hot_water",
    type="HOT_WATER_CONSUMPTION",
    yearlyDemandHeat_kWh=2000,
)
House_other_electricity = ElectricConsumptionAsset(
    name="House_other_electricity",
    type="ELECTRICITY_DEMAND",
    yearlyDemandElectricity_kWh=11000,
)


class Office_other_electricity(ElectricConsumptionAsset):
    name = "Office_other_electricity"
    type = ConsumptionAssetTypeEnum.electricity_demand
    yearlyDemandElectricity_kWh = 12000000.0


class Store_other_electricity(ElectricConsumptionAsset):
    name = "Store_other_electricity"
    type = ConsumptionAssetTypeEnum.electricity_demand
    yearlyDemandElectricity_kWh = 35000.0


class Diesel_Truck(DieselVehicleAsset):
    # eta_r=1,
    name = "Diesel_Truck"
    energyConsumption_kWhpkm = 3.0
    vehicleScaling = 10


Diesel_Vehicle = DieselVehicleAsset(
    # type=ConsumptionAssetTypeEnum.diesel_vehicle,
    # eta_r=1,
    name="Diesel_Vehicle",
    energyConsumption_kWhpkm=0.8,
    vehicleScaling=1,
)
