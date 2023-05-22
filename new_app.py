import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from dash_bootstrap_components.themes import BOOTSTRAP

from components import (
    input_components,
    output_components,
    layout_component,
)


input_fields = input_components.AppInputs()
output_fields = output_components.AppOutput()


app = dash.Dash(external_stylesheets=[BOOTSTRAP])
app.title = "Sample Size Calculator"
app.layout = layout_component.create_layout(app)


@app.callback(Output("var_selection", "children"), Input("method_radio", "value"))
def update_input_fields(value):
    return input_fields.update_output(value, input_fields.render_variable_selection)


@app.callback(
    Output("test_output", "children"),
    Input("input_button", "n_clicks"),
    State("method_radio", "value"),
    State("t_alpha", "value"),
    State("t_beta", "value"),
    State("t_delta", "value"),
    State("t_tails", "value"),
    prevent_initial_call=True,
)
def update_output_field(n_clicks, selected_test, t_alpha, t_beta, t_delta, t_tails):
    return output_fields.update_output(selected_test, t_alpha, t_beta, t_delta, t_tails)


app.run_server(debug=True)
