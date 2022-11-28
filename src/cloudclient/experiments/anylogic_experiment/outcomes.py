import json
import pandas as pd


class Outcomes:
    @property
    def outcomes(self):
        return self._outcomes

    @outcomes.setter
    def outcomes(self, outputs):
        self._outcomes = {
            outcome["human_key"]: self._calc_value(outputs, outcome)
            for outcome in self.experiment.outcomes
        }

    def write_outcomes(self):
        for outcome in self.experiment.outcomes:
            if outcome["writeExcel"]:
                self._write_outcomeExcel(outcome)
            if outcome["writeJSON"]:
                self._write_outcomeJSON(outcome)
            if outcome["print"]:
                print(self.outcomes[outcome["human_key"]])

    def _write_outcomeExcel(self, outcome):
        self.outcomes[outcome["human_key"]].to_excel(
            self._output_folder()
            / f"{outcome['human_key']}_{self.experiment.name}.xlsx"
        )

    def _write_outcomeJSON(self, outcome, formatted: bool = True):

        with open(
            self._output_folder()
            / f"{outcome['human_key']}_{self.experiment.name}.json",
            "w",
        ) as outfile:
            if formatted:
                outfile.write(
                    json.dumps(
                        json.loads(
                            self.outcomes[outcome["human_key"]].to_json(
                                orient="records"
                            )
                        ),
                        indent=2,
                    )
                )
                # print("_write jsons exported")
            else:
                outfile.writelines(
                    json.loads(
                        [self.outcomes[outcome["human_key"]]].to_json(orient="records")
                    )
                )

    def _output_folder(self):
        path = self.experiment.path / "output" / self.experiment.name
        path.mkdir(exist_ok=True, parents=True)
        return path

    def _calc_value(self, outputs, outcome):
        value = json.loads(outputs.value(outcome["anylogic_key"]))
        if outcome.get("action", "") == "normalise":
            return value / value.sum()
        return value
