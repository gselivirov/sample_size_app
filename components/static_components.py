import dash
import dash_bootstrap_components as dbc
import dash_latex
from dash import dcc, html


def render_navbar() -> dbc.NavbarSimple:
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Sample Size",
        brand_href="#",
        color="dark",
        dark=True,
    )


def render_intro_text() -> dbc.Col:
    return dbc.Col(
        [
            html.Br(),
            html.H1("Sample Size Calculators for Essential Tests"),
            html.P(
                """
            This dashboard provides easy-to-use sample size calculators for common statistical tests:
            t-tests, ANOVA, regression analysis, and chi-squared.
            """
            ),
            html.Div(
                [
                    html.Hr(),  # style={"display": "flex", "justify-content": "center"}
                    html.Br(),
                ]
            ),
        ]
    )


