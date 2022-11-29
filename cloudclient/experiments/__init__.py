import pandas as pd

from .anylogic_experiment import AnyLogicExperiment
from .experiment_settings import ExperimentSettings
from .experiment import Experiment
from im_sorry import *
from conftest import *
import etm_service
from pathlib import Path
import json


"""TODO: install pandas and check if everything works!"""
ETM_CONFIG_PATH = Path(__file__).resolve().parents[1] / "services"
ETM_CONFIG_FILE_GET_KPIS = "etm_kpis.config"
ETM_CONFIG_FILE_COSTS = "etm_costs.config"
ETM_CONFIG_FILE_SCALING = "etm_scaling.config"
COSTS_SCENARIO_ID = 2166341  # KEV + 1 MW grid battery | ETM sceanrio on beta


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

    print('calculate area-costs holon_config', experiment_inputs)
    print('calculate area-costs holon_config', experiment_outputs)

    print(experiment_outputs['APIOutputTotalCostData'])
    #experiment_outputs = experiment_outputs['APIOutputTotalCostData']
    experiment_outputs = experiment_outputs['APIOutputTotalCostData'].values.tolist()
    #experiment_outputs.type()
    real_inputs = holon_config()

    print('expected type', type(real_inputs))
    print('offered type', type(experiment_inputs))
 
    print('real inputs ', real_inputs)
    print('offered inputs ', experiment_inputs)

    #experiment_inputs2 = experiment_inputs.replace("null", "None")  
    experiment_inputs2 = json.loads(experiment_inputs)
    print('offered inputs2 ', experiment_inputs2)

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

