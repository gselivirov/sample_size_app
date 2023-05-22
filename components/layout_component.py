import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
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
                        ],
                    ),
                ],
                id="content_container",
            ),
        ],
    )
