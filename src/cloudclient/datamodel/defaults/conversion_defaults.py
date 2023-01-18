from cloudclient.datamodel import (
    ElectricCoversionAsset,
    ChemicalHeatConversionAsset,
    TransportHeatConversionAsset,
    VehicleConversionAsset,
    ConversionAssetTypeEnum,
)

House_heatpump_MT_S = TransportHeatConversionAsset(
    name="House_heatpump_MT_S",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=4,
    eta_r=0.5,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)

House_heatpump_MT_M = TransportHeatConversionAsset(
    name="House_heatpump_MT_M",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=6,
    eta_r=0.6,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)

House_heatpump_MT_L = TransportHeatConversionAsset(
    name="House_heatpump_MT_L",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=11,
    eta_r=0.6,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)
Diesel_Truck = VehicleConversionAsset(
    type="DIESEL_VEHICLE",
    eta_r=1,
    name="Diesel_Truck",
    energyConsumption_kWhpkm=3,
    vehicleScaling=10,
)

class House_gas_burner(ChemicalHeatConversionAsset):
    name = "House_gas_burner"
    type = ConversionAssetTypeEnum.gas_burner
    capacityHeat_kW = 30.0
    eta_r = 0.95
    deliveryTemp_degc = 90.0


House_DH_heatdeliveryset = ChemicalHeatConversionAsset(
    name="House_DH_heatdeliveryset",
    type="HEAT_DELIVERY_SET",
    capacityHeat_kW=10,
    eta_r=0.99,
    deliveryTemp_degc=90,
)

Electrolyser = ElectricCoversionAsset(
    name="Electrolyser",
    type="ELECTROLYSER",
    capacityElectricity_kW=100,
    eta_r=0.6,
)

DH_gas_burner_S = ChemicalHeatConversionAsset(
    name="DH_gas_burner_S",
    type="GAS_BURNER",
    capacityHeat_kW=300,
    eta_r=0.95,
    deliveryTemp_degc=90,
)

DH_heat_pump_HT_S = TransportHeatConversionAsset(
    name="DH_heat_pump_HT_S",
    type="HEAT_PUMP_GROUND",
    capacityElectricity_kW=100,
    eta_r=0.5,
    deliveryTemp_degc=90,
    ambientTempType="GROUND",
)

DH_boiler_L = ChemicalHeatConversionAsset(
    name="DH_boiler_L",
    type="BOILER",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degc=100,
)

Industrial_methane_furnace = ChemicalHeatConversionAsset(
    name="Industrial_methane_furnace",
    type="METHANE_FURNACE",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degc=120,
)

Industrial_hydrogen_furnace = ChemicalHeatConversionAsset(
    name="Industrial_hydrogen_furnace",
    type="HYDROGEN_FURNACE",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degc=120,
)


class Building_gas_burner(ChemicalHeatConversionAsset):
    name = "Building_gas_burner"
    type = ConversionAssetTypeEnum.gas_burner
    capacityHeat_kW = 60.0
    eta_r = 0.95
    deliveryTemp_degc = 90.0


Building_heatpump_20kW = TransportHeatConversionAsset(
    name="Building_heatpump_20kW",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=20,
    eta_r=0.6,
    deliveryTemp_degc=60,
    ambientTempType="AIR",
)
