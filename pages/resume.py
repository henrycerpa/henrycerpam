import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0, name="Resume")

image_path = 'assets/profile.png'
logo_one = 'assets/glare.png'
logo_two = 'assets/monkum.png'
logo_three = 'assets/ica.png'


layout = html.Div([




    dbc.Row(
        [
            dbc.Col(html.Img(src=image_path,
                    style={'position': 'center', 'width': '10%', 'left': '50px', 'top': '50px'}), style={'textAlign': 'center'}, width=0),
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('An Industrial Engineer, bringing experience in data wrangling, statistical analysis and reporting to the table. \n '
                                'My expertise in numerical simulation, utilizing various techniques and Python libraries, \n '
                                'coupled with my proficiency in data visualization tools make me a valuable asset.\n'
                                'My passion for artificial intelligence developments drives my desire \n'
                                'to stay current with industry trends and advancements.\n', style={'textAlign': 'center', 'white-space': 'pre'},
                             className='ms-3'), width=0)
        ]),

        dbc.Row(
        [
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'left'}), width=4),
            dbc.Col(dcc.Markdown('## Experience', style={'color':'#e27f04', 'textAlign': 'center', 'white-space': 'pre'},
                                 className='ms-3')),
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
        ]),

    dbc.Row(
        [   dbc.Col(html.Img(src=logo_one),
                    style={'position': 'relative', 'width': '10%', 'left': '0px', 'top': '0px'}, width=2),
            dbc.Col(dcc.Markdown('## Data Specialist \n'
                             '##### Glare Data Services \n'
                             'Since Nov/21\n', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('Successfully spearheaded the migration of data visualization tools, resulting in a 81% reduction in client costs. \n'
                                 'TECHNOLOGIES: \n'
                                 '◾Programming Languages: Python\n'
                                 '◾Declarative Language: SQL\n'
                                 '◾Spreadsheet Applications: Excel, Google Sheets\n'
                                 '◾Libraries: Pandas, Numpy, GeoJson, Dash, Plotly, Scipy , Matplotlib, Scikit-Learn\n'
                                 '◾Data visualization: Dash - Plotly, PowerBi\n'
                                 '◾Models used: Inventory management models, Discrete event simulation, Agent-based modeling\n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),

    dbc.Row(
        [   dbc.Col(html.Img(src=logo_two),
                    style={'position': 'relative', 'width': '10%', 'left': '0px', 'top': '0px'}, width=2),
            dbc.Col(dcc.Markdown('## Data Analyst \n'
                                 '##### Monkum \n'
                                 'May/19 - Oct/21 \n', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('Improve operational efficiency by successfully automating data entry, cleanup, analysis, and visualization processes\n'
                                 'with a Python migration. This resulted in a dramatic reduction of lead time from 17 to 1 day. \n'
                                 'TECHNOLOGIES: \n'
                                 '◾Programming Languages: Python\n'
                                 '◾Spreadsheet Applications: Excel, Google Sheets\n'
                                 '◾Libraries: Pandas, Numpy, Matplotlib, Scikit-Learn\n'
                                 '◾Data visualization: Tableu \n'
                                 '◾Models used: Asset-liability management\n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),

    dbc.Row(
        [dbc.Col(html.Img(src=logo_two),
                 style={'position': 'relative', 'width': '10%', 'left': '0px', 'top': '0px'}, width=2),
         dbc.Col(dcc.Markdown('## Digital Forensic Auditor \n'
                              '##### Monkum \n'
                              'Mar/16 - Apr/19 \n', style={'textAlign': 'right'}), width=2),
         dbc.Col(dcc.Markdown('Recovery of $912 million COP from the analysis of transactional data. \n'
                              'TECHNOLOGIES: \n'
                              '◾Data Processing App: SAP \n'
                              '◾Spreadsheet Applications: Excel\n'
                              '◾Data visualization: Dashboard in Excel \n'
                              '◾Models used: Monte Carlo simulation\n', style={'white-space': 'pre'},
                              className='ms-3'), width=7)
         ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'left'}), width=4),
            dbc.Col(dcc.Markdown('## Apprenticeship', style={'color':'#e27f04', 'textAlign': 'center', 'white-space': 'pre'},
                                 className='ms-3')),
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
        ]),

    dbc.Row(
        [dbc.Col(html.Img(src=logo_three),
                 style={'position': 'relative', 'width': '10%', 'left': '0px', 'top': '0px'}, width=2),
         dbc.Col(dcc.Markdown('## Data Science Fellow \n'
                              '##### ICA \n'
                              'Mar/22 - Jul/22 \n', style={'textAlign': 'right'}), width=2),
         dbc.Col(dcc.Markdown('In agreement with Correlation One, to provide a data analysis tool that generates a model of brucellosis disease \n'
                              'behavior and predictions based on data taken between years 2017 and 2021. \n'
                              'TECHNOLOGIES: \n'
                              '◾Programming Languages: Python \n'
                              '◾Spreadsheet Applications: Excel\n'
                              '◾Libraries: Pandas, Numpy, GeoJson, Dash, Plotly, Scipy \n'
                              '◾Data visualization: Dash - Plotly \n'
                              '◾Models used: Spatial-Temporal Distribution\n', style={'white-space': 'pre'},
                              className='ms-3'), width=7)
         ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
            dbc.Col(dcc.Markdown('## Certifications', style={'color':'#e27f04', 'textAlign': 'center', 'white-space': 'pre'},
                                 className='ms-3')),
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'white-space': 'pre'},
                                 className='ms-3'), width=2),
            dbc.Col(html.Div('Jul/22', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Data Science \n'
                                 'Correlation One \n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),


    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'white-space': 'pre'},
                                 className='ms-3'), width=2),
            dbc.Col(html.Div('Jun/22', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Computing and Machine Learning in the Cloud with AWS \n'
                                 'Platzi \n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'white-space': 'pre'},
                                 className='ms-3'), width=2),
            dbc.Col(html.Div('May/22', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Deep Learning with Python \n'
                                 'Platzi \n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),




    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'white-space': 'pre'},
                                 className='ms-3'), width=2),
            dbc.Col(html.Div('Dec/21', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Programming Skills on Web Apps \n'
                                 'Universidad del Norte \n', style={'white-space': 'pre'},
                                 className='ms-3'),
                    width=7)
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
            dbc.Col(dcc.Markdown('## Skills', style={'color':'#e27f04', 'textAlign': 'center', 'white-space': 'pre'},
                                 className='ms-3')),
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
        ]),

    dbc.Row(
        [

            dbc.Col([dcc.Markdown('''
                * Python
                * SQL
                * ETL Process
                * Predictive Modeling
                ''')], ),
            dbc.Col([dcc.Markdown('''
                * Power Bi
                * Dash
                * Tableu
                * Excel
                ''')], ),
            dbc.Col([dcc.Markdown('''
                * Attention to Detail
                * Statistical Knowledge
                * Communication Skills
                * Time management
                ''')], ),

        ]
    ),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
            dbc.Col(dcc.Markdown('## Education', style={'color':'#e27f04', 'textAlign': 'center', 'white-space': 'pre'},
                                 className='ms-3')),
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'textAlign': 'left'}), width=2),
            dbc.Col(html.Div('Dec/04', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Industrial Engineer \n'
                                 'Universidad del Atlantico (Barranquilla - CO)\n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'textAlign': 'left'}), width=2),
            dbc.Col(html.Div('Mar/16', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Internal Control \n'
                                 'Universidad Militar Nueva Granada (Bogota - CO)\n', style={'white-space': 'pre'},
                                 className='ms-3'),
                    width=7)
        ]),

])
