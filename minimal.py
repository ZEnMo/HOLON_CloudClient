import importlib
from cloudclient.experiments.config import CONFIG_PATH
import sys

sys.path.append(CONFIG_PATH.parent / "input")


payload = importlib.import_module("mvp").payload
