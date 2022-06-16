import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from scipy import stats
import math


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
#-------

# Functions to calculate sample sizes
def calc_size_z(d,sigma,alpha=0.05):
    if alpha==0.05:
        z=-1.645
    else:
        z=-2.326
    return ((z - 0.86) * sigma / (d))**2


def calc_size_t(d,sd,df,alpha=0.05, beta=0.2):
    t = stats.t.ppf(1 - alpha, df)
    bt = stats.t.ppf(1 - beta, df)
    return ((-t -bt) * sd / (d))**2


def calc_size_multi_z(d,sigma,alpha=0.05):
    if alpha==0.05:
        z = -1.645
    else:
        z = -2.326
    return 2 / (d / ((z - 0.86) * sigma))**2


def calc_size_multi_t(d,sd,df,alpha=0.05, beta=0.2):
    t1 = stats.t.ppf(1-alpha, df)
    t2 = stats.t.ppf(1-beta, df)
    return 2 / (d / ((-t1-t2) * sd))**2
#-------

# App layout
app.layout = dbc.Container([
    #choosing type of test
    html.Div(id="type_select",children=[

        html.H1("Sample size calculator for one- and two- sample Z- and t- tests"),
        html.H2("One-tailed"),
        html.Br(),

        html.H2("Choose the type of test"),

        dcc.Dropdown(id="test_selection",
        options=[
            {"label": "One Sample Z test", "value": "Z1"},
            {"label": "Two Sample Z test", "value": "Z2"},
            {"label": "One Sample t test", "value": "t1"},
            {"label": "Two Sample t test", "value": "t2"} ]
            # ,value=3
    )]),
    #----------
    html.Br(),
    #Inputs and results for z tests
    html.Div(id = "z_tests", style = {'display': 'block'}, children =[
        dbc.Row([
            dbc.Col([
                html.H2("Choose alpha, delta and sigma for 80% power Z test", id = "z_head", style = {'display': 'block'}),
                html.Br(),
                #inputs

                html.Label("alpha - probability of type 1 error"),
                dcc.Dropdown(id = "z_alpha",
                options=[
                    {"label": "0.05", "value": 0.05},
                    {"label": "0.01", "value": 0.01}],
                    value=0.05,
                    style= {'display': 'block'}),
                html.Br(),  

                html.Label("delta - difference between means - minimum detectable effect"),
                dcc.Input(id = "z_delta", type = "number", placeholder = "delta", style = {'display': 'block'}, value=1),
                html.Br(),

                html.Label("sigma - standard deviation of the population"),
                dcc.Input(id="z_sigma", type = "number", placeholder = "sigma", style = {'display': 'block'}, value=1),
                html.Br()

            ]),

            dbc.Col([
                #outputs
                html.H2("Required sample size:"),
                html.Div(id="z1_res"),
                html.Div(id="z2_res")
            ])
        ])
    ]),
    #----------

    # Inputs and results for t tests
    html.Div(id = "t_tests", style = {'display': 'block'}, children =[
        dbc.Row([
            dbc.Col([
                html.H2("Choose delta, standard deviation, alpha, beta and degrees of freedom for t test", id = "t_head", style = {'display': 'block'}),
                html.Br(),
                #inputs
                html.Label(" delta - difference between means - minimum detectable effect"),
                dcc.Input(id = "t_delta", type = "number", placeholder = "delta", style = {'display': 'block'}, value=1),
                html.Br(),

                html.Label("standard deviation"),
                dcc.Input(id = "t_sd", type = "number", placeholder = "sd", style = {'display': 'block'}, value=1),
                html.Br(),

                html.Label("alpha - probability of type 1 error"),
                dcc.Input(id = "t_alpha", type = "number", placeholder = "alpha", style = {'display': 'block'}, value=0.05),
                html.Br(),

                html.Label("beta - probability of type 2 error"),
                dcc.Input(id = "t_beta", type = "number", placeholder = "beta", style = {'display': 'block'}, value=0.2),
                html.Br(),

                html.Label("degrees of freedom"),
                dcc.Input(id = "t_df", type = "number", placeholder = "df", style = {'display': 'block'}, value=99),
                html.Br()
            ]),

            dbc.Col([
                #outputs
                html.H2("Required sample size:"),
                html.Div(id="t1_res"),
                html.Div(id="t2_res")
            ])
        ])
    ])
    #---------
    
])
#--------------------

#callback
@app.callback(
#outpouts for z tests
[Output(component_id='z_tests', component_property='style'),

Output(component_id='z1_res', component_property='style'),
Output(component_id='z1_res', component_property="children"),

Output(component_id='z2_res', component_property='style'),
Output(component_id='z2_res', component_property="children"),
#--------------------

#outputs fot t tests
Output(component_id='t_tests', component_property='style'),

Output(component_id='t1_res', component_property='style'),
Output(component_id='t1_res', component_property="children"),

Output(component_id='t2_res', component_property='style'),
Output(component_id='t2_res', component_property="children")
#--------------------
],


[Input(component_id='test_selection', component_property='value'),

#inputs for z tests
Input(component_id='z_delta', component_property='value'),
Input(component_id='z_alpha', component_property='value'),
Input(component_id='z_sigma', component_property='value'),
#--------------------

#inputs for t tests
Input(component_id='t_delta', component_property='value'),
Input(component_id='t_sd', component_property='value'),
Input(component_id='t_alpha', component_property='value'),
Input(component_id='t_beta', component_property='value'),
Input(component_id='t_df', component_property='value')
#--------------------
])



def do_ze_thing(visibility_state, z_delta, z_alpha, z_sigma, t_delta, t_sd, t_alpha, t_beta, t_df):
    show_z = {'display': 'none'}
    show_t = {'display': 'none'}

    #visibility of blocks
    if visibility_state == "Z1" or visibility_state == "Z2":
        show_z = {'display': 'block'}
        show_t = {'display': 'none'}
    if visibility_state == "t1" or visibility_state == "t2":
        show_z = {'display': 'none'}
        show_t = {'display': 'block'}
    #---------

    #processing for z tests
    if visibility_state == "Z1":
        z1_res = math.trunc(calc_size_z(z_delta,z_sigma,z_alpha)),
        show_z1 = show_z
    else:
        z1_res = 0,
        show_z1 = {'display': 'none'}

    if visibility_state == "Z2":
        z2_res = math.trunc(calc_size_multi_z(z_delta,z_sigma,z_alpha)),
        show_z2 = show_z
    else:
        z2_res = 0,
        show_z2 = {'display': 'none'}
    #---------

    #processing for t tests
    if visibility_state == "t1":
        t1_res = math.trunc(calc_size_t(t_delta, t_sd, t_df, t_alpha, t_beta))
        show_t1 = show_t
    else:
        t1_res = 0,
        show_t1 = {'display': 'none'}

    if visibility_state == "t2":
        t2_res = math.trunc(calc_size_multi_t(t_delta, t_sd, t_df, t_alpha, t_beta))
        show_t2 = show_t
    else:
        t2_res = 0,
        show_t2 = {'display': 'none'}
    #---------
    
    #returning values to layout
    return [show_z, #1 output - visibility of z test block
           show_z1, #2 output - visibility of result for 1 sample z test
           z1_res, #3 output - result of 1 sample z test
           show_z2, #4 output - visibility of result for 3 sample z test
           z2_res, #5 output - result of 2 sample z test

           #outputs for t tests
           show_t, #6 output - visibility of t test block
           show_t1, #7 output - visibility of result for 1 sample t test
           t1_res, #8 output - result of 1 sample t test
           show_t2, #9 output - visibility of result for 2 sample t test
           t2_res, #10 output - result of 2 sample z test
           ]
    #---------


#--------------------
if __name__ == '__main__':
    app.run_server(debug=True)

