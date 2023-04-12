import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar

dash.register_page(__name__, title='ICA', order=1, name="Portfolio")

df = pd.read_csv('assets/Berlin_crimes.csv')

def layout():
    return html.Div([




    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('Under Construction', style={'textAlign':'center'}),
                    dcc.Dropdown(id='district_chosen',
                                 options=df['District'].unique(),
                                 value=["Lichtenberg", "Pankow", "Spandau"],
                                 multi=True,
                                 style={'color':'black'}
                                 ),
                    html.Hr(),
                    dcc.Graph(id='line_chart', figure={}),

                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])



