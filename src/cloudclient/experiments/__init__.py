from .anylogic_experiment import AnyLogicExperiment
from .experiment_settings import ExperimentSettings
from .experiment import Experiment

# from .ETM_costs_data import etm_costs
from .cost_module import *
import etm_service
from pathlib import Path
import json
from .anylogic_kpis import calculate_holon_kpis

"""TODO: install pandas and check if everything works!"""
ETM_CONFIG_PATH = Path(__file__).resolve().parents[1] / "services"
ETM_CONFIG_FILE_GET_KPIS = "etm_kpis.config"
ETM_CONFIG_FILE_COSTS = "etm_costs.config"
ETM_CONFIG_FILE_SCALING = "etm_scaling.config"
# COSTS_SCENARIO_ID = 2166341  # KEV + 1 MW grid battery | ETM sceanrio on beta
COSTS_SCENARIO_ID = 1661972  # KEV 2030 standaard preset id


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
    calculateAllKPIs(api_experiment)


def calculateAllKPIs(api_experiment: AnyLogicExperiment):
    grid_connection_config = json.loads(
        api_experiment.client.inputs.get_input("P grid connection config JSON")
    )
    gridnode_config = json.loads(
        api_experiment.client.inputs.get_input("P grid node config JSON")
    )

    experiment_outputs = api_experiment.outcomes.get("APIOutputTotalCostData")
    hourly_curves = api_experiment.outcomes.get("APIOutputHourlyCurvesData")
    print("\nExperiment output categories:", experiment_outputs[0].keys())
    print("\n")

    etm_costs_stored = np.load("ETM_costs.npy", allow_pickle=True).tolist()

    areaCosts_kEur = calculate_total_costs_split(
        # etm_service.retrieve_results(
        #     COSTS_SCENARIO_ID, ETM_CONFIG_PATH, ETM_CONFIG_FILE_COSTS
        # ),
        etm_costs_stored,
        grid_connection_config,
        experiment_outputs[0],
        hourly_curves[0],
    )
    print("\nTotal area costs:")
    print(areaCosts_kEur, " kEur")

    etm_production_data_stored = np.load(
        "ETM_production_data.npy", allow_pickle=True
    ).tolist()

    area_KPI_results = calculate_holon_kpis(
        total_cost_data=experiment_outputs[0],
        hourly_curves=hourly_curves[0],
        etm_data=etm_production_data_stored,
        # etm_data=etm_service.retrieve_results(
        #     COSTS_SCENARIO_ID, ETM_CONFIG_PATH, ETM_CONFIG_FILE_GET_KPIS
        # ),
        gridnode_config=json.loads(
            api_experiment.client.inputs.get_input("P grid node config JSON")
        ),
    )
    print("\n Gebieds-kpi's: ")
    print(area_KPI_results)

    # print(
    #     "\nETM upscale sliders dict: ",
    #     api_experiment.client.payload.etm_upscale_sliders,
    # )

    # api_experiment.client.payload.etm_upscale_curve_labels.keys(): hourly_curves[0][
    #     api_experiment.client.payload.etm_upscale_curve_labels.values()
    # ]

    # print(holon_curves_for_upscaling)

    if api_experiment.experiment.upscale_ETM:
        # ETM upscaling to national level
        # etm_slider_settings = {}  # This dict should come from the case definition!
        # etm_slider_settings.update(
        #     {
        #         "share_of_electric_trucks": 100,
        #         "installed_energy_grid_battery": 0,
        #     }
        # )
        # print("ETM slider settings:", etm_slider_settings)
        holon_curves_for_upscaling = {}
        try:
            for key in api_experiment.client.payload.etm_upscale_curve_labels.keys():
                holon_curves_for_upscaling.update(
                    {
                        key: hourly_curves[0][
                            api_experiment.client.payload.etm_upscale_curve_labels[key]
                        ]
                    }
                )
            # holon_curves_for_upscaling = {
            #     "totalEHGVHourlyChargingProfile_kWh": hourly_curves[0][
            #         "totalEHGVHourlyChargingProfile_kWh"
            #     ],
            #     "totalGridBatteryHourlyChargingProfile_kWh": hourly_curves[0][
            #         "totalBatteryHourlyChargingProfile_kWh"
            #     ],
            # }
        except KeyError:
            print("etm_kpi_holon_output: Resolving to empty values for this key!")

        # print("holon_output: ", holon_output)  # , " and size: ", size(holon_output))

        etm_upscale_scenario_id = etm_service.scale_copy_and_send(
            COSTS_SCENARIO_ID,
            api_experiment.client.payload.etm_upscale_sliders
            | holon_curves_for_upscaling,
            ETM_CONFIG_PATH,
            ETM_CONFIG_FILE_SCALING,
        )
        etm_upscale_results = etm_service.retrieve_results(
            etm_upscale_scenario_id, ETM_CONFIG_PATH, ETM_CONFIG_FILE_GET_KPIS
        )

        # print("\nETM upscale results: ", etm_upscale_results)

        results = {
            "netload": round(etm_upscale_results["national_kpi_network_load"], 1),
            "costs": round(
                etm_upscale_results["national_total_costs"], -8
            ),  # reduce significance
            # ETM returns factor instead of percentage for sustainability
            "sustainability": round(
                100 * etm_upscale_results["national_renewability"], 1
            ),
            "self_sufficiency": round(
                etm_upscale_results["national_kpi_self_sufficiency"], 1
            ),
        }

        print("\n ETM nationale KPIs:")
        print(results)


# pd.set_option("display.max_rows", 50000)
# pd.set_option("display.expand_frame_repr", True)
# pd.set_option('display.width', 1000)
# print("expected type", type(real_inputs))
# print("offered type", type(experiment_inputs))

# print("real inputs ", real_inputs)
# print("offered inputs ", experiment_inputs)

# experiment_inputs2 = experiment_inputs.replace("null", "None")

# print("offered inputs2 ", grid_connection_config)
# print("Hourly curves type:", type(hourly_curves[0]))

# print("Hourly curves categories:", hourly_curves[0].keys())
# result = calculate_total_costs(etm_output(), holon_config(), holon_output())
