import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./00_data/2019.csv')

app = dash.Dash()
features = df.columns


app.layout = html.Div([
    html.H1('World Happiness Rankings'),
    html.H2('Select X and Y axes'),
    html.Div([
        dcc.Dropdown(id='xaxis',
                     options=[{'label': i, 'value': i} for i in features],
                     value='GDP per capita')
    ], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        dcc.Dropdown(id='yaxis',
                     options=[{'label': i, 'value': i} for i in features],
                     value='Healthy life expectancy')
    ], style={'width': '48%', 'display': 'inline-block'}),
    dcc.Graph(id='feature-graphic')
], style={'padding': 10})


@app.callback(Output('feature-graphic', 'figure'),
              [Input('xaxis', 'value'),
               Input('yaxis', 'value')])
def update_graph(xaxis_name, yaxis_name):
    return {'data': [go.Scatter(x=df[xaxis_name],
                                y=df[yaxis_name],
                                text=df['Country'],
                                mode='markers',
                                marker={'size': 15},
                                )
                     ],
            'layout': go.Layout(title='World Happiness Rankings',
                                xaxis={'title': xaxis_name},
                                yaxis={'title': yaxis_name},
                                hovermode='closest'), }


if __name__ == '__main__':
    app.run_server()
