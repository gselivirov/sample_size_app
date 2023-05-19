import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from dash_bootstrap_components.themes import BOOTSTRAP

from components import static_components, input_components, output_components


input_fields = input_components.AppInputs()
output_fields = output_components.AppOutput()


def create_layout(app: dash.Dash):
    return html.Div(
        className="layout_cont",
        children=[
            static_components.render_navbar(),
            dbc.Container(
                [
                    dbc.Row([static_components.render_intro_text()]),
                    dbc.Row(
                        [
                            dbc.Col(
                                input_fields.render(),
                                width=5,
                            ),
                            dbc.Col(output_fields.render()),
                        ]
                    ),
                ],
                id="content_container",
            ),
        ],
    )


app = dash.Dash(external_stylesheets=[BOOTSTRAP])
app.title = "Sample Size Calculator"
app.layout = create_layout(app)


@app.callback(Output("var_selection", "children"), Input("method_radio", "value"))
def update_input_fields(value):
    return input_fields.update_output(value, input_fields.render_variable_selection)


app.run_server(debug=True)