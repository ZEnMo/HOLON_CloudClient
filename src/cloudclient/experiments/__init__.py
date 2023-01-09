from .anylogic_experiment import AnyLogicExperiment
from .experiment_settings import ExperimentSettings
from .experiment import Experiment

from .cost_module import *
from .ETM_dummy_data import etm_output
import etm_service
from pathlib import Path
import json


def run_all():
    """Runs all experiments"""
    experiments = ExperimentSettings.load()
    for experiment_setting in experiments.all():
        start_experiment(experiment_setting)


def run_one(experiment_name):
    experiments = ExperimentSettings.load()
    start_experiment(experiments.find(experiment_name))


def run_one_scenario(experiment_name, inputs=None):

    experiments = ExperimentSettings.load()
    settings = experiments.get(
        experiment_name, experiments.experiments[experiment_name]
    )

    experiment = Experiment(**settings)

    # Run experiment in AnyLogic Cloud
    api_experiment = AnyLogicExperiment(experiment)
    outcome = api_experiment.runScenario(inputs=inputs)

    return outcome


def prepare_scenario_as_experiment(experiment_name: str) -> AnyLogicExperiment:
    """Supply the name of the experiment as defined in experiments.yml and get a prepared AnylogicExperiment"""
    experiments = ExperimentSettings.load()
    settings = experiments.get(
        experiment_name, experiments.experiments[experiment_name]
    )
    return AnyLogicExperiment(Experiment(**settings))


def start_experiment(settings):
    """Runs one experiments"""
    experiment = Experiment(**settings)

    # Run experiment in AnyLogic Cloud
    api_experiment = AnyLogicExperiment(experiment)

    if experiment.query_api:
        api_experiment.runSimulation()
    print("\nDuration: ", api_experiment.duration_s, " seconds\n")
    # return api_experiment
    calculateAreaCosts(api_experiment)


def calculateAreaCosts(api_experiment):
    grid_connection_config_json = api_experiment.client.inputs.get_input(
        "P grid connection config JSON"
    )
    experiment_outputs = api_experiment.outcomes.get("APIOutputTotalCostData")
    hourly_curves = api_experiment.outcomes.get("APIOutputHourlyCurvesData")
    # print('calculate area-costs holon_config', api_experiment.client.inputs.get_input('P grid connection config JSON'))
    # print('calculate area-costs holon_output', api_experiment.outcomes.get('APIOutputTotalCostData'))

    # pd.set_option("display.max_rows", 50000)
    # pd.set_option("display.expand_frame_repr", True)
    # pd.set_option('display.width', 1000)

    # print("Print experiment inputs: ", experiment_inputs)
    # print("Print experiment outputs: ", experiment_outputs[0])

    # print(experiment_outputs["APIOutputTotalCostData"])
    # experiment_outputs = experiment_outputs['APIOutputTotalCostData']
    # experiment_outputs = experiment_outputs["APIOutputTotalCostData"].values.tolist()
    # experiment_outputs = experiment_outputs[0].values.tolist()
    # experiment_outputs.type()

    # real_inputs = holon_config()
    # real_inputs = experiment_inputs

    # print("expected type", type(real_inputs))
    # print("offered type", type(experiment_inputs))

    # print("real inputs ", real_inputs)
    # print("offered inputs ", experiment_inputs)

    # experiment_inputs2 = experiment_inputs.replace("null", "None")
    grid_connection_config = json.loads(grid_connection_config_json)
    # print("offered inputs2 ", grid_connection_config)
    # print("Hourly curves type:", type(hourly_curves[0]))
    print("\nExperiment output categories:", experiment_outputs[0].keys())
    # print("Hourly curves categories:", hourly_curves[0].keys())
    # result = calculate_total_costs(etm_output(), holon_config(), holon_output())
    result = calculate_total_costs(
        etm_output(), grid_connection_config, experiment_outputs[0], hourly_curves[0]
    )
    print("Total area costs: ", result, " kEur")
