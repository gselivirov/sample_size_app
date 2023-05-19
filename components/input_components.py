import dash
import dash_bootstrap_components as dbc
from dash import dcc, html


class AppInputs:
    def __init__(self):
        self.vars_t_test = [
            {"var_name": "Alpha", "var_id": "var_1"},
            {"var_name": "Standard deviation", "var_id": "var_2"},
        ]

        self.vars_anova = [
            {"var_name": "anova1", "var_id": "var_a_1"},
            {"var_name": "anova2", "var_id": "var_a_2"},
        ]

    def create_input_field(self, var_name: str, var_id: str) -> dbc.Row:
        return dbc.Row(
            [
                dbc.Col(html.P(var_name), width=3),
                dbc.Col(
                    dbc.Input(
                        type="number", size="sm", style={"width": "40%"}, id=var_id
                    )
                ),
            ]
        )

    def render_variable_selection(self, test_name: str) -> list:
        if test_name == "t_test":
            variables = self.vars_t_test
        elif test_name == "anova":
            variables = self.vars_anova

        return [
            html.H4("Input Variables"),
            dbc.Container(
                [
                    self.create_input_field(
                        var_name=f'{item["var_name"]}: ', var_id=item["var_id"]
                    )
                    for item in variables
                ]
            ),
        ]

    def render(self) -> list:
        return [
            html.H3("Select Test"),
            html.P("Select one of suggested options."),
            dbc.Container(
                [
                    dbc.RadioItems(
                        id="method_radio",
                        options=[
                            {"label": "t-test", "value": "t_test"},
                            {"label": "ANOVA", "value": "anova"},
                            {"label": "Regression", "value": "regr"},
                            {"label": "Chi-squared", "value": "chi"},
                        ],
                        value="t_test",
                    )
                ]
            ),
            html.Br(),
            html.Div(id="var_selection"),
        ]

    def update_output(self, selected_test, func):
        return func(selected_test)
