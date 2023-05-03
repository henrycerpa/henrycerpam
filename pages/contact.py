import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3, name="Email & Contact")

green_text = {'color':'green'}

email = 'assets/email.png'
telegram = 'assets/telegram.png'
linkedin = 'assets/linkedin.png'
github = 'assets/github.png'
youtube = 'assets/youtube.png'
twitch = 'assets/twitch.png'
tiktok = 'assets/tiktok.png'

def layout():
    return html.Div([
        html.H2("Email & Contact Info", style={'textAlign': 'center'}, className='my-3'),
        html.Hr(style={'color': '#e27f04', }),

        dbc.Row([
            dbc.Col([
                html.Img(src=email,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[henrycerpa@outlook.com](mailto:henrycerpa@outlook.com)', link_target='_blank'),

            ], width=3),
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Img(src=telegram,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[Message me in Telegram](https://t.me/henrycerpa)', link_target='_blank'),

            ], width=3),
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Img(src=linkedin,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[Go to my LinkedIn user](https://www.linkedin.com/in/henrycerpa/)', link_target='_blank'),

            ], width=3),
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Img(src=github,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[Go to my GitHub repositories](https://github.com/henrycerpa)', link_target='_blank'),

            ], width=3),
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Img(src=youtube,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[Go to my YouTube channel](https://www.youtube.com/@datahenry)', link_target='_blank'),

            ], width=3),
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Img(src=twitch,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[Go to my Twitch channel](https://www.twitch.tv/datahenry)', link_target='_blank'),

            ], width=3),
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Img(src=tiktok,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[Go to my Tik Tok user](https://www.tiktok.com/@datahenry)', link_target='_blank'),

            ], width=3),
        ], justify='center'),








    ])
