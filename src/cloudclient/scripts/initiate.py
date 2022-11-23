import os
import yaml
import shutil
import sys
from pathlib import Path


CONFIG_FOLDER = Path(__file__).parent.parent / "config"


def pprint(prompt):
    print("[HOLON-cloudclient]: " + prompt)


def create_folder(folder_location: str = None, get_api_key: bool = None) -> None:

    if folder_location is None:
        args = sys.argv[1:]
        if not ("-tf" in args or "--target-folder" in args):
            raise SystemExit(
                "Please provide the target folder using the [-tf | --target-folder] option to specify the relative location of the .cloudclient folder."
            )
        else:
            for i, arg in enumerate(args):
                if "-tf" in arg or "--target-folder" in arg:
                    try:
                        target_folder = args[i + 1]
                    except IndexError:
                        raise SystemError(
                            "Option [-tf | --target-folder] is supplied but no value is supplied!"
                        )
    abs_target = Path().resolve().absolute().__str__() + "\\target_folder"
    pprint(f"Initiating cloudclient... \t (at {abs_target})")

    # make folders
    BASE_PATH = Path(target_folder + "/.cloudclient")
    BASE_PATH.mkdir(exist_ok=True, parents=True)
    CONFIG_PATH = BASE_PATH / "config"
    CONFIG_PATH.mkdir(exist_ok=True, parents=True)
    (BASE_PATH / "input").mkdir(exist_ok=True, parents=True)
    (BASE_PATH / "ouput").mkdir(exist_ok=True, parents=True)

    # move files
    shutil.copy2(
        CONFIG_FOLDER / "config.example.yml",
        CONFIG_PATH / "config.yml",
    )
    shutil.copy2(
        CONFIG_FOLDER / "experiments.example.yml",
        CONFIG_PATH / "experiments.yml",
    )
    # add a pointer to the new top folder
    with open(CONFIG_FOLDER / ".cloudclient_location.yml", "w") as f:
        yaml.dump({"file_path": str(CONFIG_PATH.absolute())}, f)

    pprint("Done!")

    if get_api_key is None:
        if "--get-apikey" in args:
            update_config_yaml(CONFIG_PATH / "config.yml")
        else:
            pprint(
                "No api_key is supplied. Either add it to 'cloudclient/config/config.yml' or get it from OS by adding the [--get-apikey] to the options."
            )


def update_config_yaml(config_path: Path) -> None:

    from cloudclient.experiments.config import Config

    config = Config.load(config_path)
    config["anylogic_cloud"]["api_key"] = os.environ["AL_API_KEY"]

    config.dump(config_path)
