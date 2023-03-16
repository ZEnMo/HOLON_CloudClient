import numpy as np
import csv

ETM_share_of_renewable_electricity = {}
ETM_CO2_intensity_of_electricity = {}

for i in range(8760):
    key = str(i)
    value1 = 0.5
    value2 = 0.6
    ETM_share_of_renewable_electricity[key] = value1
    ETM_CO2_intensity_of_electricity[key] = value2
    

def determine_share_of_renewables(etm_data: dict) -> np.ndarray:
    # TODO: move this to the ETsource repo as a gquery

    renewables = np.array(
        [
            etm_data["hourly_supply_electricity_from_biogas"],
            etm_data["hourly_supply_electricity_from_biomass"],
            etm_data["hourly_supply_electricity_from_geothermal"],
            etm_data["hourly_supply_electricity_from_greengas"],
            etm_data["hourly_supply_electricity_from_hydro"],
            etm_data["hourly_supply_electricity_from_hydrogen"],
            etm_data["hourly_supply_electricity_from_solar"],
            etm_data["hourly_supply_electricity_from_uranium"],
            etm_data["hourly_supply_electricity_from_waste"],
            etm_data["hourly_supply_electricity_from_wind"],
        ]
    ).sum(axis=0)
    total = np.array(etm_data["hourly_production_electricity"])
    
    return renewables / total


def calculate_holon_kpis(
    simulation_results: dict, hourly_curves: dict, etm_data: dict, gridnode_config: dict
) -> dict:

    import_curve_MWh = np.array(
        list(hourly_curves["SystemHourlyElectricityImport_MWh"].values())[:8760]
    )

    total_CO2_imported_electricity_kg = np.inner(
        etm_data["CO2_curve"], import_curve_MWh
    )

    # # TODO: now hard coded; replace by a query
    # etm_data.update({"CO2diesel_kgpMWh": 323, "CO2methane_kgpMWh": 1890 / 9})

    # CO2totaal = (
    #     total_CO2_imported_electricity_kg
    #     + total_cost_data["totalMethaneImport_MWh"] * etm_data["CO2methane_kgpMWh"]
    #     + total_cost_data["totalDieselImport_MWh"] * etm_data["CO2diesel_kgpMWh"]
    # )
    #
    share_of_renewables = determine_share_of_renewables(etm_data=etm_data)
    print("form of ETM-data")
    print(share_of_renewables)

    np.savetxt('share_of_renewables.csv', share_of_renewables, delimiter=',')

    UnsustainableImportedElectricity_MWh = np.inner(
        1 - share_of_renewables, import_curve_MWh
    )

    Sustainability_pct = 100 * (
        1
        - (
            simulation_results["totalDieselImport_MWh"]
            + simulation_results["totalMethaneImport_MWh"]
            + UnsustainableImportedElectricity_MWh
        )
        / simulation_results["TotalEnergyUsed_MWh"]
    )
    Sustainability_pct = min(100, Sustainability_pct)

    MSLS_capacity_kW = sum(
        [gn["capacity_kw"] for gn in gridnode_config if gn["type"] == "MSLS"]
    )
    netload_mv_pos_pct = (
        (simulation_results["MSLSnodePeakPositiveLoadElectricity_kW"])
        / MSLS_capacity_kW
    ) * 100

    netload_mv_neg_pct = (
        (simulation_results["MSLSnodePeakNegativeLoadElectricity_kW"])
        / MSLS_capacity_kW
    ) * 100

    KPIs = {
        "sustainability": round(Sustainability_pct, 1),
        "self_sufficiency": round(
            simulation_results["totalSelfSufficiency_fr"] * 100, 1
        ),
        "+ netload MV": round(netload_mv_pos_pct, 1),
        "- netload MV": round(netload_mv_neg_pct, 1),
    }
    print("version: anylogic_kpis_new")
    return KPIs
