import pandas as pd
from pandas import json_normalize

from .anylogic_experiment import AnyLogicExperiment
from .experiment_settings import ExperimentSettings
from .experiment import Experiment
from im_sorry import *
from conftest import *
import etm_service
from pathlib import Path
import json
from anylogic_kpi import calculate_holon_kpis


"""TODO: install pandas and check if everything works!"""
ETM_CONFIG_PATH = Path(__file__).resolve().parents[1] / "services"
ETM_CONFIG_FILE_GET_KPIS = "etm_kpis.config"
ETM_CONFIG_FILE_COSTS = "etm_costs.config"
ETM_CONFIG_FILE_SCALING = "etm_scaling.config"
#COSTS_SCENARIO_ID = 2166341  # KEV + 1 MW grid battery | ETM sceanrio on beta
#COSTS_SCENARIO_ID = 2171115 # standaard NL
COSTS_SCENARIO_ID = 1661972 # KEV 2030 standaard preset id

def run_all():
    """Runs all experiments"""
    experiments = ExperimentSettings.load()
    for experiment_setting in experiments.all():
        start_experiment(experiment_setting)

def run_one(experiment_name):
    experiments = ExperimentSettings.load()
    start_experiment(experiments.find(experiment_name))


def run_one_scenario(experiment_name, inputs):

    experiments = ExperimentSettings.load()
    settings = experiments.get(
        experiment_name, experiments.experiments[experiment_name]
    )

    experiment = Experiment(**settings)

    # Run experiment in AnyLogic Cloud
    api_experiment = AnyLogicExperiment(experiment)
    outcome = api_experiment.runScenario(inputs)
        
    return outcome


def start_experiment(settings):
    """Runs one experiments"""
    experiment = Experiment(**settings)
    print(experiment)

    # Run experiment in AnyLogic Cloud
    api_experiment = AnyLogicExperiment(experiment)
    
    if experiment.query_api:
        #api_experiment.client.client.get_model_by_id("277499ea-5bee-48ad-90f8-41ef3ae395e7")
        api_experiment.runSimulation()

    print("\nDuration: ", api_experiment.duration_s, " seconds\n")
    #return api_experiment
    calculateAreaCosts(api_experiment)

def calculateAreaCosts(api_experiment):
    experiment_inputs = api_experiment.client.inputs.get_input('P grid connection config JSON')
    experiment_outputs = api_experiment.outcomes.get('APIOutputTotalCostData')
    #print('calculate area-costs holon_config', api_experiment.client.inputs.get_input('P grid connection config JSON'))
    #print('calculate area-costs holon_output', api_experiment.outcomes.get('APIOutputTotalCostData'))
    
    #pd.set_option("display.max_rows", 50000)
    #pd.set_option("display.expand_frame_repr", True)
    #pd.set_option('display.width', 1000)

    #print('calculate area-costs holon_config', experiment_inputs)
    #print('calculate area-costs holon_config', experiment_outputs)

    #print(experiment_outputs['APIOutputTotalCostData'])
    #experiment_outputs = experiment_outputs['APIOutputTotalCostData']
    experiment_outputs = experiment_outputs['APIOutputTotalCostData'].values.tolist()
    #experiment_outputs.type()
    real_inputs = holon_config()

    #print('expected type', type(real_inputs))
    #print('offered type', type(experiment_inputs))
 
    #print('real inputs ', real_inputs)
    #print('offered inputs ', experiment_inputs)

    #experiment_inputs2 = experiment_inputs.replace("null", "None")  
    experiment_inputs2 = json.loads(experiment_inputs)
    #print('offered inputs2 ', experiment_inputs2)

    print(COSTS_SCENARIO_ID)
    print(ETM_CONFIG_PATH)
    print(ETM_CONFIG_FILE_COSTS)
    etm_service.retrieve_results(COSTS_SCENARIO_ID, ETM_CONFIG_PATH, ETM_CONFIG_FILE_COSTS)
    

    #print('etm output ', etm_service.retrieve_results(COSTS_SCENARIO_ID, ETM_CONFIG_PATH, ETM_CONFIG_FILE_COSTS) )
    # result = calculate_total_costs(etm_output(), holon_config(), holon_output())
    #result = calculate_total_costs(etm_output(), experiment_inputs2, experiment_outputs[0])
    result = calculate_total_costs_split(etm_output(), experiment_inputs2, experiment_outputs[0])
    
    #result = calculate_total_costs( etm_service.retrieve_results(COSTS_SCENARIO_ID, ETM_CONFIG_PATH, ETM_CONFIG_FILE_COSTS), experiment_inputs2, experiment_outputs[0])
    print(result)
    
    
    total_cost_data = api_experiment.outcomes.get('APIOutputTotalCostData')
    print("data  :")
    total_cost_data = total_cost_data.get("APIOutputTotalCostData")
    total_cost_data_zero = total_cost_data[0]
    total_cost_data_zero = total_cost_data_zero[0]
    #total_cost_data_zero = json.dumps(total_cost_data_zero)

    #print("data zero: ")
    #print( total_cost_data_zero ) 
    #total_cost_data_zero = dict.fromkeys(total_cost_data_zero)
    #print(total_cost_data_zero)
    #print(total_cost_data_zero['totalSelfSufficiency_fr'])
    #print(total_cost_data_zero["SystemHourlyElectricityImport_MWh"])
    #print(total_cost_data.get(""))
    #holon_output = json_normalize(total_cost_data.get("0")) 
    
    #list(total_cost_data["SystemHourlyElectricityImport_MWh"].values())[:8760]

    #print(holon_output)
    #total_cost_data = pd.DataFrame(api_experiment.outcomes.get('APIOutputTotalCostData'))
    #etm_service.retrieve_results(COSTS_SCENARIO_ID, ETM_CONFIG_PATH, ETM_CONFIG_FILE_SCALING)

    #print(experiment_inputs2)

    kpiresults = calculate_holon_kpis(
                    total_cost_data=total_cost_data_zero,
                    etm_data=etm_service.retrieve_results(COSTS_SCENARIO_ID, ETM_CONFIG_PATH, ETM_CONFIG_FILE_GET_KPIS), 
                    gridnode_config = json.loads( api_experiment.client.inputs.get_input('P grid node config JSON') ),
                )
    print("gebieds-kpi's: ")
    print(kpiresults)
