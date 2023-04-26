# HOLON cloudclient module

This repo contains the (legacy) AnyLogic cloudclient implementation of the HOLON project. This repo and other repos are licensed under the [MIT license](LICENSE.md). Other repos are:

1. [AnyLogic](https://github.com/ZEnMo/HOLON)
2. [ETM service](https://github.com/ZEnMo/HOLON-ETM)
3. [webapp](https://github.com/ZEnMo/HOLON-webapp)

(works better at the [Github Pages](https://zenmo.github.io/HOLON-cloudclient/))

The experiments module allows you to define your experiment in a config file and run one or
multiple experiments sequentially. No more adjusting classes! Based on the existing scripts.

- [HOLON cloudclient module](#holon-cloudclient-module)
  - [Installation](#installation)
    - [Development](#development)
    - [Production](#production)
  - [Starting up](#starting-up)
  - [Running the module](#running-the-module)
  - [Pipenv support](#pipenv-support)
  - [Data classes](#data-classes)
    - [Examples](#examples)

## Installation

### Development

Uses editable wheel build.

```bash
git clone https://github.com/ZEnMo/HOLON-cloudclient.git
cd HOLON-cloudclient
# CREATE AND ACTIVATE YOUR ENV OF CHOICE
pip install -e .
cloudclient_init --target-folder .
```

### Production

**Direct**

```bash
pip install git+https://github.com/ZEnMo/HOLON-cloudclient@main#egg=cloudclient
cloudclient_init --target-folder folder/for/clouclient/config --get-api-key # asumes "AL_API_KEY" in env vars
```

**Via requirements.txt**

```
git+https://github.com/ZEnMo/HOLON-cloudclient@main#egg=cloudclient
```

## Starting up

The `cloudclient_init` command that you issued during installation links the `cloudclient` package to your project configuration folder `.cloudclient`. This folder contains the information that is used by the package to run experiments on the AnyLogic private cloud.

Go to the `config` folder and open `config.yml`. Specify your secret API key to connect to the AnyLogic Cloud there.

```yaml
anylogic_cloud:
  api_key: 7a3563c1-ea1c-41d6-8009-b7abfd93f7ba
  url: https://engine.holontool.nl
```

Go to the `config` folder and open `experiments.yml`. Specify
your experiments there.

```yaml
<experiment_name>:
  model_name:     name of the anylogic model to connect to
  config_file:    the excel database file or ::cloudclient.datamodel:: from which to read the config sheets
  timestep_hours: Float, timestep in hours
  force_uncached: True | False, force the anylogic model to run in uncached mode
  show_progress:  True | False, ?
  parallelize:    True | False, allow the model to run in paralellized mode
  log_exceptions: True | False, log exceptions or not
  use_datamodel:  True | False, whether to treat the input as a ::cloudclient.datamodel::
  inputs:         list (optional), list the anylogic input key and the file in
                  which to find the inputs for each input
                  See format below
                  - anylogic_key: <key>
                    file: <sheetname> or <datamodel.Payload attribute> to submit to the key
                    write: True | False

  outcome:        list, name all the outcoems that should be taken from the model.
                  They become accesible and will be saved under their human_key
                  Specify if they should be written to a file, or printed out.
                  Also allows for actions on the data. Currently only normalise is
                  avaibale.
```

## Running the module

The base code for the module is in the `experiments` folder. But you can easily call the module
from the script `run_experiments` in the `scripts` folder. Here you can run one experiment by
specifying its name or all experiments by using the keyword `ALL`.

## Pipenv support

There is also support for pipenv now for the ones that are interested. There is a shortcut to
run the experiments: `pipenv run experiments {experiment_name}`.

Happy experimenting!

## Data classes

Data classes are used to structure and validate data before it is sent to the AnyLogic API. Find the class diagrams below:

1. [Conversion assets](doc/html/conversion_classes.html)
2. [Consumption assets](doc/html/consumption_classes.html)
3. [Storage assets](doc/html/storage_classes.html)
4. [Production assets](doc/html/production_classes.html)
5. [Grid connections](doc/html/gridconnections_classes.html)
6. [Gridnode assets](doc/html/gridnodes_classes.html)
7. [Actors](doc/html/actors_classes.html)
8. [Contracts](doc/html/contracts_classes.html)

### Examples

Check out the example JSON file over at: [doc/assets/example.json](doc/assets/example.json).

Or inspect the visual representation below:
![](doc/img/example.png)
