from cloudclient.experiments import Experiment, ExperimentSettings
from cloudclient.experiments import AnyLogicExperiment

experiments = ExperimentSettings.load()

experiment_setting = next(experiments.all())
experiment = Experiment(**experiment_setting)
api_experiment = AnyLogicExperiment(experiment)
