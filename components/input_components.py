import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.test_info_components import t_test, anova




class AppInputs:
    def __init__(self):
        self.tests = {
            t_test.value: t_test,
            anova.value: anova,
        }

    def create_input_field(self, var_name: str, var_id: str) -> dbc.Row:
        return dbc.Row(
            [
                dbc.Col(html.P(var_name), width=4),
                dbc.Col(
                    dbc.Input(
                        type="number", size="sm", style={"width": "40%"}, id=var_id, value=0
                    )
                ),
            ],
        )

    def render_variable_selection(self, test_name: str) -> list:
        return [
            html.H4("Input Variables", id="input_header"),
            dbc.Container(
                [
                    self.create_input_field(
                        var_name=f'{item.name}: ', var_id=item.id
                    )
                    for item in self.tests[test_name].vars
                ]
            ),
        ]

    def render(self) -> list:
        options = []
        for test in self.tests.values():
            options.append({"label": test.label, "value": test.value})

        return [
            html.H3("Select Test"),
            html.P("Select one of suggested options."),
            dbc.Container(
                [
                    dbc.RadioItems(
                        id="method_radio",
                        options=options,
                        value=list(self.tests.keys())[0],
                        inputCheckedClassName="border border-dark bg-dark",
                    )
                ]
            ),
            html.Br(),
            html.Div(id="var_selection"),
            dbc.Button("Calculate", color="dark", id="input_button"),
        ]

    def update_output(self, selected_test: str, func: callable):
        return func(selected_test)
