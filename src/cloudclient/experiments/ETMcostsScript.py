# Script to retreive ETM cost data
import etm_service
import json
import numpy as np
from pathlib import Path

"""TODO: install pandas and check if everything works!"""
ETM_CONFIG_PATH = Path(__file__).resolve().parents[1] / "services"
# ETM_CONFIG_FILE_GET_KPIS = "etm_kpis.config"
ETM_CONFIG_FILE_COSTS = "etm_costs.config"
# ETM_CONFIG_FILE_SCALING = "etm_scaling.config"
# COSTS_SCENARIO_ID = 2166341  # KEV + 1 MW grid battery | ETM sceanrio on beta
COSTS_SCENARIO_ID = 1661972  # KEV 2030 standaard preset id

etm_cost_data = etm_service.retrieve_results(
    COSTS_SCENARIO_ID, ETM_CONFIG_PATH, ETM_CONFIG_FILE_COSTS
)

## Manual overrides of specific values!
etm_cost_data["depreciation_costs_grid_battery_per_mwh"] = 80
etm_cost_data["depreciation_costs_wind_farm_per_kw"] = 25
# print(etm_cost_data)

# Save to file
np.save("ETM_costs.npy", etm_cost_data)

# etm_cost_loaded = np.load("ETM_costs.npy", allow_pickle=True).tolist()
# print(etm_cost_loaded)

# print(etm_cost_loaded["depreciation_costs_grid_battery_per_mwh"])
