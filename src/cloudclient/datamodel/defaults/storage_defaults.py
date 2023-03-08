from cloudclient.datamodel import (
    HeatStorageAsset,
    ElectricStorageAsset,
    VehicleElectricStorageAsset,
    StorageAssetTypeEnum,
)

House_battery = ElectricStorageAsset(
    name="House_battery",
    type="STORAGE_ELECTRIC",
    capacityElectricity_kW=10,
    stateOfCharge_r=1.0,
    storageCapacity_kWh=50,
)

House_heatmodel_A = HeatStorageAsset(
    name="House_heatmodel_A",
    type="HEATMODEL",
    capacityHeat_kW=100.0,
    #stateOfCharge_r=0.5,
    initial_temperature_degC = 20,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=50,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_B = HeatStorageAsset(
    name="House_heatmodel_B",
    type="HEATMODEL",
    capacityHeat_kW=100.0,
    #stateOfCharge_r=0.5,
    initial_temperature_degC = 20,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=60,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_C = HeatStorageAsset(
    name="House_heatmodel_C",
    type="HEATMODEL",
    capacityHeat_kW=100.0,
    #stateOfCharge_r=0.5,
    initial_temperature_degC = 20,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=70,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_D = HeatStorageAsset(
    name="House_heatmodel_D",
    type="HEATMODEL",
    capacityHeat_kW=100.0,
    #stateOfCharge_r=0.5,
    initial_temperature_degC = 20,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=80,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_E = HeatStorageAsset(
    name="House_heatmodel_E",
    type="HEATMODEL",
    capacityHeat_kW=100.0,
    #stateOfCharge_r=0.5,
    initial_temperature_degC = 20,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=90,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_F = HeatStorageAsset(
    name="House_heatmodel_F",
    type="HEATMODEL",
    capacityHeat_kW=100.0,
    #stateOfCharge_r=0.5,
    initial_temperature_degC = 20,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=100,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
House_heatmodel_G = HeatStorageAsset(
    name="House_heatmodel_G",
    type="HEATMODEL",
    capacityHeat_kW=100.0,
    #stateOfCharge_r=0.5,
    initial_temperature_degC = 20,
    minTemp_degC=-10,
    maxTemp_degC=50,
    setTemp_degC=20,
    lossFactor_WpK=110,
    heatCapacity_JpK=10000000.0,
    ambientTempType="AIR",
)
EV = VehicleElectricStorageAsset(
    name="EV",
    type="ELECTRIC_VEHICLE",
    capacityElectricity_kW=7.0,
    stateOfCharge_r=1.0,
    storageCapacity_kWh=60.0,
    energyConsumption_kWhpkm=0.3,
    vehicleScaling=1,
)
EHGV = VehicleElectricStorageAsset(
    name="EHGV",
    type="ELECTRIC_VEHICLE",
    stateOfCharge_r=1.0,
    storageCapacity_kWh=500,
    capacityElectricity_kW=100,
    energyConsumption_kWhpkm=1.1,
    vehicleScaling=10,
)

House_heat_buffer = HeatStorageAsset(
    name="Household heat buffer",
    type="STORAGE_HEAT",
    capacityHeat_kW=4.0,
    #stateOfCharge_r=0.75,
    initial_temperature_degC=70,
    minTemp_degC=55,
    maxTemp_degC=80,
    setTemp_degC=60,
    lossFactor_WpK=0.0,
    heatCapacity_JpK=1200000.0,
    ambientTempType="AIR",
)

District_Heating_heat_buffer_HT_S = HeatStorageAsset(
    name="District_Heating_heat_buffer_HT_S",
    type="STORAGE_HEAT",
    capacityHeat_kW=2000.0,
    #stateOfCharge_r=0.75,
    initial_temperature_degC = 90,
    minTemp_degC=70,
    maxTemp_degC=100,
    setTemp_degC=90,
    lossFactor_WpK=3,
    heatCapacity_JpK=120000000.0,
    ambientTempType="GROUND",
)

District_Heating_heat_buffer_MT_S = HeatStorageAsset(
    name="District_Heating_heat_buffer_MT_S",
    type="STORAGE_HEAT",
    capacityHeat_kW=2000.0,
    #stateOfCharge_r=0.75,
    initial_temperature_degC = 70,
    minTemp_degC=60,
    maxTemp_degC=80,
    setTemp_degC=70,
    lossFactor_WpK=3,
    heatCapacity_JpK=120000000.0,
    ambientTempType="GROUND",
)

District_Heating_network_HT_S = HeatStorageAsset(
    name="District_Heating_network_HT_S",
    type="STORAGE_HEAT",
    capacityHeat_kW=1000.0,
    #stateOfCharge_r=1.0,
    initial_temperature_degC = 90,
    minTemp_degC=70,
    maxTemp_degC=100,
    setTemp_degC=90,
    lossFactor_WpK=100,
    heatCapacity_JpK=10000000.0,
    ambientTempType="GROUND",
)

District_Heating_network_HT_L = HeatStorageAsset(
    name="District_Heating_network_HT_L",
    type="STORAGE_HEAT",
    capacityHeat_kW=1000.0,
    #stateOfCharge_r=1.0,
    initial_temperature_degC = 90,
    minTemp_degC=70,
    maxTemp_degC=100,
    setTemp_degC=90,
    lossFactor_WpK=10000,
    heatCapacity_JpK=1000000000.0,
    ambientTempType="GROUND",
)

District_Heating_network_LT_L = HeatStorageAsset(
    name="District_Heating_network_LT_L",
    type="STORAGE_HEAT",
    capacityHeat_kW=1000.0,
    #stateOfCharge_r=1.0,
    initial_temperature_degC = 15,
    minTemp_degC=10,
    maxTemp_degC=30,
    setTemp_degC=15,
    lossFactor_WpK=10000,
    heatCapacity_JpK=1000000000.0,
    ambientTempType="GROUND",
)

District_Heating_network_MT_S = HeatStorageAsset(
    name="District_Heating_network_MT_S",
    type="STORAGE_HEAT",
    capacityHeat_kW=1000.0,
    #stateOfCharge_r=1.0,
    initial_temperature_degC = 70,
    minTemp_degC=60,
    maxTemp_degC=80,
    setTemp_degC=70,
    lossFactor_WpK=100,
    heatCapacity_JpK=10000000.0,
    ambientTempType="GROUND",
)

District_Heating_network_MT_L = HeatStorageAsset(
    name="District_Heating_network_MT_S",
    type="STORAGE_HEAT",
    capacityHeat_kW=1000.0,
    #stateOfCharge_r=1.0,
    initial_temperature_degC = 70,
    minTemp_degC=60,
    maxTemp_degC=80,
    setTemp_degC=70,
    lossFactor_WpK=10000,
    heatCapacity_JpK=1000000000.0,
    ambientTempType="GROUND",
)

class Grid_battery(ElectricStorageAsset):
    # capacityElectricity_kW: float
    storageCapacity_kWh = 10000.0
    capacityElectricity_kW = storageCapacity_kWh * 0.2
    name = "Grid_battery"
    type = StorageAssetTypeEnum.storage_electric
    # capacityElectricity_kW = (2000,)
    stateOfCharge_r = 0.5
    # storageCapacity_kWh=10000,


Grid_battery_7MWh = ElectricStorageAsset(
    name="Grid_battery_7MWh",
    type="STORAGE_ELECTRIC",
    capacityElectricity_kW=2000,
    stateOfCharge_r=0.5,
    storageCapacity_kWh=7000,
)

Grid_battery_10MWh = ElectricStorageAsset(
    name="Grid_battery_10MWh",
    type="STORAGE_ELECTRIC",
    capacityElectricity_kW=2000,
    stateOfCharge_r=0.5,
    storageCapacity_kWh=10000,
)
