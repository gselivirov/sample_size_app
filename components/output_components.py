import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from statsmodels.stats.power import tt_ind_solve_power
from components.test_info_components import DataInterface

data_interface = DataInterface()


class AppOutput:
    def __init__(self):
        self.tests = data_interface.tests

    def render(self) -> list:
        return [
            dbc.Container(
                dbc.Card(
                    [
                        dbc.CardHeader("Card header"),
                        dbc.CardBody(
                            [
                                html.H5(
                                    "Card title",
                                    className="card-title",
                                    id="test_output",
                                ),
                                html.Div(id="size"),
                                html.P(
                                    "This is some card content that we'll reuse",
                                    className="card-text",
                                ),
                            ]
                        ),
                    ],
                    color="dark",
                    outline=True,
                )
            )
        ]

    def update_output(self, selected_test, values):
        variables = {
            variable.id: value for variable, value in zip(self.tests[selected_test].vars, values)
        }

        return self.tests[selected_test].func(**variables)