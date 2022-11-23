from os import sys, path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

RESULT_OPTIONS = [
    "timeStep_h",
    "timeStepsElapsed",
    "modelHoursElapsed_h",
    "modelStartUpDuration_s",
    "modelRunDuration_s",
    "nGridNodes",
    "nGridConnections",
    "nEnergyAssets",
    "nConnectionOwners",
    "nEnergySuppliers",
    "nEnergyHolons",
    "nAdministrativeHolons",
    "nGridOperators",
    "nNationalEnergyMarket",
    "totalElectricityImported_MWh",
    "totalElectricityExported_MWh",
]


from experiments import run_one_scenario


def run_scenario_endpoint(
    scenario: str, inputs: dict, results: list[str] = RESULT_OPTIONS
):

    # loads the scenario (experiment in current AL module), overwrites inputs and returns all outcomes
    outcomes = run_one_scenario(experiment_name=scenario, inputs=inputs)

    # desired result validation
    for result in results:
        if result not in RESULT_OPTIONS:
            raise KeyError(
                f"Invalid outcome key provided! Valid keys: {RESULT_OPTIONS}"
            )

    # filters outcomes and only passes the desired outputs (cols in pd.df)
    results = outcomes["APIOutputRunData"][results]

    # returns the desired as a dict
    return results.to_dict(orient="records")[0]


if __name__ == "__main__":

    # these variables would be send from the front end to the endpoint
    # interactive input ||
    capacity_electric_kw = 0
    # defined in the CMS, contained in the storyline ||
    results = ["totalElectricityImported_MWh", "totalElectricityExported_MWh"]
    scenario = "webdev_cloud_poc"

    # this would be the back end function trigger
    response = run_scenario_endpoint(
        scenario=scenario,
        inputs={
            "P energy assets config JSON": {
                "index": 0,
                "agenttype": "energyAsset",
                "id": "a1",
                "type": "PRODUCTION",
                "type2": "WINDMILL",
                "parent": "b25",
                "capacity_electric_kw": capacity_electric_kw,
                "capacity_heat_kw": 0,
            }
        },
        # results=results,
    )

    # this would be the response
    print(response)
