import pandas as pd
import os
from dash import Dash
from dash_html_components import Div, H1, Img
from dash_core_components import Dropdown
from dash.dependencies import Input, Output

caminho = os.path.dirname(__file__)
arquivo = caminho + r"\nba.csv"

data = pd.read_csv(rf"{arquivo}")

posicoes ={'Armador': 'PG', 'Ala-armador': 'SG', 'Ala': 'SF', 'Ala de força': 'PF', 'Pivô': 'C'}

app = Dash(__name__)

app.layout = Div(
    id='div-principal',
    children=[
        H1(
            'Maiores pontuadores da NBA',
            id='titulo'
        ),

        Dropdown(
            id='opcoes-jogadores',
            options=[
                {'label': '1º Lugar', 'value': 0},
                {'label': '2º Lugar', 'value': 1},
                {'label': '3º Lugar', 'value': 2},
                {'label': '4º Lugar', 'value': 3},
                {'label': '5º Lugar', 'value': 4},
                {'label': '6º Lugar', 'value': 5},
                {'label': '7º Lugar', 'value': 6},
                {'label': '8º Lugar', 'value': 7},
                {'label': '9º Lugar', 'value': 8},
                {'label': '10º Lugar', 'value': 9}
            ],
            value= 9,
            style={
                'font-family': ['Poppins', 'sans-serif'],
                'width': '200px',
                'margin': 'auto',
                'text-align': 'center',
                'border': 'none',
                'border-radius': '5px'
            }
        ),

        Div(
            id='div-jogador',
            children=[
                Div(
                    id='quadrados',
                    children=[
                        Div(id='quadrado1'),
                        Div(id='quadrado2'),
                        Div(
                            id='quadrado3',
                            children=[
                                Img(src='assets/quadrado3.png')
                            ]
                        ),
                        Div(
                            id='quadrado-imagem',
                            children=[

                            ]
                        )
                    ]
                ),

                Div(
                    id='info',
                    children=[
                        Div(
                            className='info-jogador',
                            children=[
                                H1(
                                    'NOME',
                                    className='labels-info'
                                ),
                                H1(
                                    id='nome',
                                    className='infos'
                                )
                            ]
                        ),
                        Div(
                            className='info-jogador',
                            children=[
                                H1(
                                    'POSIÇÃO',
                                    className='labels-info'
                                ),
                                H1(
                                    id='posicao',
                                    className='infos'
                                )
                            ]
                        ),
                        Div(
                            className='info-jogador',
                            children=[
                                H1(
                                    'PONTOS',
                                    className='labels-info'
                                ),
                                H1(
                                    id='pontos',
                                    className='infos'
                                )
                            ]
                        )
                    ]
                )
            ]
        ),


    ]
)

@app.callback(
    [
        Output('quadrado-imagem', 'children'),
        Output('nome', 'children'),
        Output('posicao', 'children'),
        Output('pontos', 'children')
    ],
    Input('opcoes-jogadores', 'value')
)

def meu_callback(meu_input):
    return Img(src=f'assets/{data["player"][meu_input]}.png'),\
        data['player'][meu_input],\
        data['position'][meu_input],\
        data['total_points'][meu_input]

app.run_server()
