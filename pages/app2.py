import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from .side_bar import sidebar
from sklearn.linear_model import LogisticRegression

dash.register_page(__name__, name="Cannabis in California", title='Cannabis Sales')

df = pd.read_csv('https://raw.githubusercontent.com/henrycerpa/database/main/CannabisSalesByCounty.csv')
data = pd.read_csv('https://raw.githubusercontent.com/henrycerpa/database/main/midwestern_hemp.csv')
data = data.sort_index()

# Calculate high THC failures (0 for pass, 1 for failure).
data['fail'] = (data['total_thc'] >= 0.3).astype(int)

# Create dummy variables for categorical features.
X = pd.get_dummies(data[['state', 'county', 'sample_date']])

# Target variable
y = data['fail']

# Train the logistic regression model
logreg = LogisticRegression()
logreg.fit(X, y)


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
                    html.Div([
                        html.Div([
                            html.P([
                                'Understanding market trends and sales is crucial in legal cannabis market. In this case, being aware of market trends and sales data allows businesses to identify consumer preferences, anticipate demand and adjust their production and distribution accordingly.'],
                                style={'color': 'BLACK', 'font-size': '15px'})
                        ], style={'width': '180%'}),
                    ], className='footer', style={'display': 'flex'}),

                    html.H2("Per Capita Cannabis Sales by County in California", style={'text-align': 'center'}),
                    html.H3("Select a County"),
                    dcc.Dropdown(
                        id='county-dropdown',
                        options=[{'label': county, 'value': county} for county in df['County'].unique()],
                        value=df['County'].unique()[0]
                    ),
                    dcc.Graph(id='sales-graph'),

                    html.Div([
                        html.Div([
                            html.P([
                                'Introducing the "Hemp Failure Rate Prediction" tool: This allows you to predict the failure rate of hemp samples based on state, county, and sample date information. Simply enter the relevant details and click the button to get the predicted failure rate.'],
                                style={'color': 'BLACK', 'font-size': '15px'})
                        ], style={'width': '180%'}),
                    ], className='footer', style={'display': 'flex'}),

                    html.H2("Hemp Failure Rate Prediction", style={'text-align': 'center'}),
                    html.Div([
                        html.Label("State"),
                        dcc.Input(id='state-input', type='text'),
                        html.Label("County"),
                        dcc.Input(id='county-input', type='text'),
                        html.Label("Sample Date"),
                        dcc.DatePickerSingle(id='date-input', date=None),
                        html.Button('Predict Failure Rate', id='predict-button', n_clicks=0),
                        html.Div(id='prediction-output')
                    ])

                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])


@callback(
    dash.dependencies.Output('sales-graph', 'figure'),
    [dash.dependencies.Input('county-dropdown', 'value')]
)
def update_graph(selected_county):
    filtered_data = df[df['County'] == selected_county]
    filtered_data['YearQuarter'] = filtered_data['Calendar Year'].astype(str) + ' Q' + filtered_data['Quarter'].astype(
        str)
    filtered_data = filtered_data.sort_values('YearQuarter')  # Ordenar los valores en el eje X
    fig = px.line(filtered_data, x='YearQuarter', y='Per Capita Sales', color='County')
    fig.update_layout(
        yaxis={'title': 'Per Capita Sales'},
        xaxis={'type': 'category'}  # Especificar que los valores en el eje X sean tratados como categorías
    )
    return fig

@callback(
    dash.dependencies.Output('prediction-output', 'children'),
    [dash.dependencies.Input('predict-button', 'n_clicks')],
    [dash.dependencies.State('state-input', 'value'), dash.dependencies.State('county-input', 'value'), dash.dependencies.State('date-input', 'date')]
)
def predict_failure_rate(n_clicks, state, county, date):
    if n_clicks > 0:
        input_data = pd.DataFrame({'state': [state], 'county': [county], 'sample_date': [date]})
        input_data = pd.get_dummies(input_data)  # Create dummy variables
        input_data = input_data.reindex(columns=X.columns, fill_value=0)  # Align columns with training data
        prediction = logreg.predict_proba(input_data)[:, 1]  # Probability of failure (class 1)
        return html.Div([
            html.H3("Predicted Failure Rate:"),
            html.P(f"{prediction[0]:.2%}")
        ])
    return ''
