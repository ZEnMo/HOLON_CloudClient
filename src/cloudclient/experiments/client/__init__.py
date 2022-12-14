from anylogiccloudclient.client.cloud_client import CloudClient
from cloudclient.experiments.config import config, CONFIG_PATH
from cloudclient.experiments.client.inputs import Inputs
import importlib
import sys
import urllib
from urllib.request import Request
from urllib.error import HTTPError
from anylogiccloudclient.client.cloud_error import CloudError
import json


class HttpClient:
    def __init__(self, root_url, api_key):
        self.root_url = root_url
        self.api_key = api_key

    def api_request(self, url, method="GET", body=None):
        try:
            request = Request(
                self.root_url + urllib.parse.quote(url),
                method=method,
                unverifiable=False,
            )
            if body is not None:
                request.data = json.dumps(body).encode("utf-8")
            self._merge_default_headers(request)
            response = urllib.request.urlopen(request)
        except HTTPError as err:
            raise CloudError.from_json(json.loads(err.read()))
        return json.loads(response.read())

    def request(self, url, method="GET", body=None):
        try:
            request = Request(self.root_url + url, method=method, unverifiable=False)
            if body is not None:
                request.data = body
            self._merge_default_headers(request)
            response = urllib.request.urlopen(request)
        except HTTPError as err:
            raise CloudError.from_json(json.loads(err.read()))
        return json.loads(response.read())

    def _merge_default_headers(self, request):
        request.add_header("Authorization", self.api_key)
        request.add_header("Content-Type", "application/json")


class Client(Inputs):
    def __init__(self, experiment):
        self.client = CloudClient(
            config["anylogic_cloud"]["api_key"], config["anylogic_cloud"]["url"]
        )
        # THIS IS NASTY! Overwrite the HTTP client used in the cloudclient module
        self.client._http_client = HttpClient(
            self.client.root_url, config["anylogic_cloud"]["api_key"]
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
