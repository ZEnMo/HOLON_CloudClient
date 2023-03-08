from cloudclient.datamodel import (
    ElectricCoversionAsset,
    ElectricHeatConversionAsset,
    ChemicalHeatConversionAsset,
    TransportHeatConversionAsset,
    VehicleConversionAsset,
    ElectricHob,
    ConversionAssetTypeEnum,
)

House_heatpump_MT_S = TransportHeatConversionAsset(
    name="House_heatpump_MT_S",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=4,
    eta_r=0.5,
    deliveryTemp_degC=65.0,
    # ambientTempType="AIR",
)

House_heatpump_water_MT_S = TransportHeatConversionAsset(
    name="House_heatpump_water_MT_S",
    type="HEAT_PUMP_WATER",
    capacityElectricity_kW=2,
    eta_r=0.5,
    deliveryTemp_degC=65.0,
    ambientTempType="WATER",
)

House_heatpump_MT_M = TransportHeatConversionAsset(
    name="House_heatpump_MT_M",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=6,
    eta_r=0.6,
    deliveryTemp_degC=65.0,
    # ambientTempType="AIR",
)

House_heatpump_MT_L = TransportHeatConversionAsset(
    name="House_heatpump_MT_L",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=11,
    eta_r=0.6,
    deliveryTemp_degC=60.0,
    # ambientTempType="AIR",
)
Diesel_Truck = VehicleConversionAsset(
    type="DIESEL_VEHICLE",
    eta_r=1,
    name="Diesel_Truck",
    energyConsumption_kWhpkm=3,
    vehicleScaling=10,
)

Diesel_Vehicle = VehicleConversionAsset(
    type="DIESEL_VEHICLE",
    eta_r=1,
    name="Diesel_Vehicle",
    energyConsumption_kWhpkm=0.7,
    vehicleScaling=1,
)


class House_gas_burner(ChemicalHeatConversionAsset):
    name = "House_gas_burner"
    type = ConversionAssetTypeEnum.gas_burner
    capacityHeat_kW = 30.0
    eta_r = 0.95
    deliveryTemp_degC = 90.0


House_DH_heatdeliveryset = ChemicalHeatConversionAsset(
    name="House_DH_heatdeliveryset",
    type="HEAT_DELIVERY_SET",
    capacityHeat_kW=30,
    eta_r=1.0,
    deliveryTemp_degC=90.0,
)

House_DH_heatdeliveryset_MT = ChemicalHeatConversionAsset(
    name="House_DH_heatdeliveryset_MT",
    type="HEAT_DELIVERY_SET",
    capacityHeat_kW=30,
    eta_r=1.0,
    deliveryTemp_degC=50.0,
)

House_eboiler_M = ElectricHeatConversionAsset(
    name="House_eboiler_M",
    type="BOILER",
    capacityElectricity_kW=20,
    eta_r=1.0,
    deliveryTemp_degC=90.0,
)


class Electrolyser(ElectricCoversionAsset):
    name = "Electrolyser"
    type = ConversionAssetTypeEnum.electrolyser
    capacityElectricity_kW = 100.0
    eta_r = 0.6


DH_gas_burner_S = ChemicalHeatConversionAsset(
    name="DH_gas_burner_S",
    type="GAS_BURNER",
    capacityHeat_kW=300,
    eta_r=0.95,
    deliveryTemp_degC=90.0,
)

DH_heat_pump_HT_S = TransportHeatConversionAsset(
    name="DH_heat_pump_HT_S",
    type="HEAT_PUMP_GROUND",
    capacityElectricity_kW=100,
    eta_r=0.5,
    deliveryTemp_degC=90.0,
    ambientTempType="GROUND",
)

DH_heat_pump_MT_S = TransportHeatConversionAsset(
    name="DH_heat_pump_HT_S",
    type="HEAT_PUMP_GROUND",
    capacityElectricity_kW=100,
    eta_r=0.5,
    deliveryTemp_degC=60.0,
    ambientTempType="GROUND",
)

DH_boiler_M = ChemicalHeatConversionAsset(
    name="DH_boiler_M",
    type="GAS_BURNER",
    capacityHeat_kW=300,
    eta_r=0.95,
    deliveryTemp_degC=90.0,
)

DH_heat_pump_MT_S = TransportHeatConversionAsset(
    name="DH_heat_pump_HT_S",
    type="HEAT_PUMP_GROUND",
    capacityElectricity_kW=100,
    eta_r=0.5,
    deliveryTemp_degC=60.0,
    ambientTempType="GROUND",
)

DH_boiler_M = ChemicalHeatConversionAsset(
    name="DH_boiler_M",
    type="GAS_BURNER",
    capacityHeat_kW=300,
    eta_r=0.95,
    deliveryTemp_degC=90.0,
)

DH_boiler_L = ChemicalHeatConversionAsset(
    name="DH_boiler_L",
    type="GAS_BURNER",
    capacityHeat_kW=600,
    eta_r=0.95,
    deliveryTemp_degC=90.0,
)

Industrial_methane_furnace = ChemicalHeatConversionAsset(
    name="Industrial_methane_furnace",
    type="METHANE_FURNACE",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degC=120.0,
)

Industrial_hydrogen_furnace = ChemicalHeatConversionAsset(
    name="Industrial_hydrogen_furnace",
    type="HYDROGEN_FURNACE",
    capacityHeat_kW=300,
    eta_r=0.99,
    deliveryTemp_degC=120.0,
)


class Building_gas_burner(ChemicalHeatConversionAsset):
    name = "Building_gas_burner"
    type = ConversionAssetTypeEnum.gas_burner
    capacityHeat_kW = 60.0
    eta_r = 0.95
    deliveryTemp_degC = 90.0


Building_heatpump_20kW = TransportHeatConversionAsset(
    name="Building_heatpump_20kW",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=20,
    eta_r=0.6,
    deliveryTemp_degC=60.0,
    ambientTempType="AIR",
)


class Curtailer(ElectricCoversionAsset):
    name = "Curtailer"
    type = ConversionAssetTypeEnum.curtailer
    capacityElectricity_kW = 10000.0
    eta_r = 0.0


Methane_CHP_M = ElectricCoversionAsset(
    name="Methane_CHP_M",
    type="METHANE_CHP",
    capacityElectricity_kW=200,
    eta_r=0.45,
)

House_water_heatpump_MT_M = TransportHeatConversionAsset(
    name="House_water_heatpump_MT_M",
    type="HEAT_PUMP_WATER",
    capacityElectricity_kW=6,
    eta_r=0.6,
    deliveryTemp_degC=60.0,
    ambientTempType="WATER",
)

DH_heat_pump_water_MT_M = TransportHeatConversionAsset(
    name="DH_heat_pump_water_MT_M",
    type="HEAT_PUMP_WATER",
    capacityElectricity_kW=200,
    eta_r=0.5,
    deliveryTemp_degC=60.0,
    ambientTempType="WATER",
)

Methane_CHP_M = ElectricHeatConversionAsset(
    name="Methane_CHP_M",
    type="METHANE_CHP",
    capacityElectricity_kW=200,
    eta_r=0.45,
    deliveryTemp_degC = 90.0,
)

House_water_heatpump_MT_M = TransportHeatConversionAsset(
    name="House_water_heatpump_MT_M",
    type="HEAT_PUMP_WATER",
    capacityElectricity_kW=6,
    eta_r=0.6,
    deliveryTemp_degC=60.0,
    ambientTempType="WATER",
)

DH_heat_pump_water_MT_M = TransportHeatConversionAsset(
    name="DH_heat_pump_water_MT_M",
    type="HEAT_PUMP_WATER",
    capacityElectricity_kW=200,
    eta_r=0.5,
    deliveryTemp_degC=60.0,
    ambientTempType="WATER",
)

Electric_hob = ElectricHob(
    name="Electric hob", 
    type="ELECTRIC_HOB", 
    eta_r=0.3,
    capacityElectricity_kW=5.0)