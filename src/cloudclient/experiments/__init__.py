import pandas as pd

from .anylogic_experiment import AnyLogicExperiment
from .experiment_settings import ExperimentSettings
from .experiment import Experiment

"""TODO: install pandas and check if everything works!"""


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
    api_experiment.runSimulation()

    print("\nDuration: ", api_experiment.duration_s, " seconds\n")
