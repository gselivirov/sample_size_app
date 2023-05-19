import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

class AppOutput():
    def __init__(self):
        self.input_var = None
        self.output_var = None
    
    def render(self) -> list:
        return [
            html.Div(id='out_put')
        ]

    def update_output(self, input_var, func):
        pass