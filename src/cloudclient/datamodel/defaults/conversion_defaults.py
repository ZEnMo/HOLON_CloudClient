from cloudclient.datamodel import (
    ElectricConversionAsset,
    ChemicalConversionAsset,
    ChemicalHeatConversionAsset,
    TransportHeatConversionAsset,
    # VehicleConversionAsset,
    ConversionAssetTypeEnum,
)

House_heatpump_MT_S = TransportHeatConversionAsset(
    name="House_heatpump_MT_S",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=4,
    eta_r=0.5,
    deliveryTemp_degC=60.0,
    # ambientTempType="AIR",
)

House_heatpump_MT_M = TransportHeatConversionAsset(
    name="House_heatpump_MT_M",
    type="HEAT_PUMP_AIR",
    capacityElectricity_kW=6,
    eta_r=0.6,
    deliveryTemp_degC=60.0,
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
    eta_r=0.99,
    deliveryTemp_degC=90.0,
)


class Electrolyser(ElectricConversionAsset):
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
    # ambientTempType="GROUND",
)

DH_heat_pump_MT_S = TransportHeatConversionAsset(
    name="DH_heat_pump_HT_S",
    type="HEAT_PUMP_GROUND",
    capacityElectricity_kW=100,
    eta_r=0.5,
    deliveryTemp_degC=60.0,
    # ambientTempType="GROUND",
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
    # ambientTempType="GROUND",
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


class Industrial_hydrogen_furnace(ChemicalHeatConversionAsset):
    name = "Industrial_hydrogen_furnace"
    type = ConversionAssetTypeEnum.hydrogen_furnace
    capacityHeat_kW = 300.0
    eta_r = 0.99
    deliveryTemp_degC = 120.0


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
    # ambientTempType="AIR",
)


class Curtailer(ElectricConversionAsset):
    name = "Curtailer"
    type = ConversionAssetTypeEnum.curtailer
    capacityElectric_kW = 10000.0
    eta_r = 0.0


House_water_heatpump_MT_M = TransportHeatConversionAsset(
    name="House_water_heatpump_MT_M",
    type="HEAT_PUMP_WATER",
    capacityElectricity_kW=6,
    eta_r=0.6,
    deliveryTemp_degC=60.0,
    # ambientTempType="GROUND",
)

DH_heat_pump_water_MT_M = TransportHeatConversionAsset(
    name="DH_heat_pump_water_MT_M",
    type="HEAT_PUMP_WATER",
    capacityElectricity_kW=200,
    eta_r=0.5,
    deliveryTemp_degC=60.0,
    # ambientTempType="GROUND",
)

Methane_CHP_M = ChemicalConversionAsset(
    name="Methane_CHP_M",
    type="METHANE_CHP",
    capacityMethane_kW=400,
    eta_r=0.45,
)


House_water_heatpump_MT_M = TransportHeatConversionAsset(
    name="House_water_heatpump_MT_M",
    type="HEAT_PUMP_WATER",
    capacityElectricity_kW=6,
    eta_r=0.6,
    deliveryTemp_degC=60.0,
    # ambientTempType="GROUND",
)

DH_heat_pump_water_MT_M = TransportHeatConversionAsset(
    name="DH_heat_pump_water_MT_M",
    type="HEAT_PUMP_WATER",
    capacityElectricity_kW=200,
    eta_r=0.5,
    deliveryTemp_degC=60.0,
    # ambientTempType="GROUND",
)

# Electric_hob = Electric_heater(name="Electric hob", type="ELECTRIC_HOB", capacity_kW=5.0)
Electric_hob = ElectricConversionAsset(
    type=ConversionAssetTypeEnum.electric_heater,
    capacityElectric_kW=5.0,
    name="Electric hob",
    eta_r=0.7,
)
