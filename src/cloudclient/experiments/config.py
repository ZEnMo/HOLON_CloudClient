from pathlib import Path
import yaml


class Config(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def load(cls, path):
        with open(path, "r") as f:
            doc = yaml.load(f, Loader=yaml.FullLoader)
        return cls(doc)

    def dump(self, path):
        with open(path, "w") as f:
            yaml.dump(dict(self), f)
        return None


file_path = Config.load(
    Path(__file__).parent.parent / "config/.cloudclient_location.yml"
)["file_path"]
CONFIG_PATH = Path(file_path)

config = Config.load(CONFIG_PATH / "config.yml")
