from anylogiccloudclient.client.cloud_client import CloudClient
from cloudclient.experiments.config import config, CONFIG_PATH
from cloudclient.experiments.client.inputs import Inputs
import importlib
import sys


class Client(Inputs):
    def __init__(self, experiment):
        self.client = CloudClient(
            config["anylogic_cloud"]["api_key"], config["anylogic_cloud"]["url"]
        )
        
        # the order matters!
        self.experiment = experiment
        # init the data model if required:
        if self.experiment.use_datamodel is True:
            self.load_datamodel()

        self.inputs = experiment.model_name

    def run_simulation(self, polling_period=10):
        """Returns the runs outputs TODO: polling period is hardcoded"""
        return self.client.create_simulation(self.inputs).get_outputs_and_run_if_absent(
            polling_period=polling_period
        )

    def load_datamodel(self):
        """Imports the module that contains the data model definition and sets it as attribute in json form"""
        input_path = CONFIG_PATH.parent / self.experiment.config_file
        module = input_path.stem

        # TODO: This is technical debt for sure!
        sys.path.append(str(input_path.parent.absolute()))
        payload = importlib.import_module(module).payload
        self.datamodel_payload = payload.to_json()

        # remove the appended path part
        _ = sys.path.pop(-1)
