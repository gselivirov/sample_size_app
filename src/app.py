import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html, ALL
from dash_bootstrap_components.themes import BOOTSTRAP

from components import (
    input_components,
    output_components,
    layout_component,
)


input_fields = input_components.AppInputs()
output_fields = output_components.AppOutput()


app = dash.Dash(__name__, external_stylesheets=[BOOTSTRAP])
server = app.server

app.title = "Sample Calculator"
app.layout = layout_component.create_layout(app)


@app.callback(Output("var_selection", "children"), Input("method_radio", "value"))
def update_input_fields(value):
    return input_fields.update_output(value, input_fields.render_variable_selection)


@app.callback(
    Output("output_container", "children"),
    Input("input_button", "n_clicks"),
    [
        State("method_radio", "value"),
        State({"type": "input_field_input", "index": ALL}, "value"),
    ],
    prevent_initial_call=True,
)
def update_output_field(n_clicks, selected_test, values):
    return output_fields.update_output(selected_test, values)


app.run_server(host='0.0.0.0')
