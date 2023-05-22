import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from statsmodels.stats.power import tt_ind_solve_power


class AppOutput:
    def __init__(self):
        self.var = None

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

    def update_output(self, selected_test, t_alpha, t_beta, t_delta, t_tails):
        size = tt_ind_solve_power(t_delta, None, t_alpha, t_beta, 1)
        return html.P(size)
