import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from components.test_info_components import DataInterface


data_interface = DataInterface()


class AppInputs:
    def __init__(self):
        self.tests = data_interface.tests

    def create_input_field(
        self, type: str, var_name: str, var_id: str, value: any
    ) -> dbc.Row:
        return dbc.Row(
            [
                dbc.Col(html.P(f"{var_name}: "), width=4),
                dbc.Col(
                    dbc.Input(
                        type=type,
                        size="sm",
                        style={"width": "40%"},
                        id={"type": "input_field_input", "index": var_id},
                        value=value,
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
                        type=item.type,
                        var_name=item.name,
                        var_id=item.id,
                        value=item.value,
                    )
                    for item in self.tests[test_name].vars
                ],
                style={"margin-top": "1rem"},
                id="variables_container",
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
                ],
                style={"margin-top": "1rem"},
            ),
            html.Br(),
            html.Div(id="var_selection"),
            dbc.Button(
                "Calculate",
                color="dark",
                id="input_button",
                style={"margin-top": "1rem"},
            ),
        ]

    def update_output(self, selected_test: str, func: callable):
        return func(selected_test)
