import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from statsmodels.stats.power import tt_ind_solve_power
from components.test_info_components import DataInterface
from components.output_interpretation_components import render_copy

data_interface = DataInterface()



class AppOutput:
    def __init__(self):
        self.tests = data_interface.tests

    def render(self) -> list:
        return [
            dbc.Container(
                id="output_container",
            )
        ]

    def update_output(self, selected_test: str, values: list) -> list:
        variables = {
            variable.id: value
            for variable, value in zip(self.tests[selected_test].vars, values)
        }

        result = int(self.tests[selected_test].func(**variables)) + 1

        return render_copy(result, selected_test, variables)


