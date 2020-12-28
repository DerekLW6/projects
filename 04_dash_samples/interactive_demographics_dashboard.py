import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('./00_data/acs2017_county_data.csv')

states = df['State'].unique()

features = df.columns
features_list = []

# Creating a features list
for j in features:
    features_list.append(j)

features_list.remove('State')
features_list.remove('CountyId')
features_list.remove('County')

app.layout = html.Div([
    html.H1('State Demographics Dashboard'),
    html.H2('Select state then X and Y axes'),
    html.H4('Counties will automatically be generated/color coded'),
    html.H4('Data Dictionary can be found here: '),
    html.H4('https://www.kaggle.com/muonneutrino/us-census-demographic-data'),
    html.Div([
        dcc.Dropdown(
            id='state',
            options=[{'label': i.title(), 'value': i} for i in states],
            value='Alabama'
        )
    ],
        style={'width': '25%', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='xaxis',
            options=[{'label': i, 'value': i} for i in features_list],
            value='Income'
        )
    ],
        style={'width': '25%', 'float': 'middle', 'display': 'inline-block'}),

    html.Div([
        dcc.Dropdown(
            id='yaxis',
            options=[{'label': i, 'value': i} for i in features_list],
            value='VotingAgeCitizen'
        )
    ], style={'width': '25%', 'float': 'middle', 'display': 'inline-block'}),

    dcc.Graph(id='feature-graphic')
], style={'padding': 10})


@app.callback(
    Output('feature-graphic', 'figure'),
    [Input('state', 'value'),
     Input('xaxis', 'value'),
     Input('yaxis', 'value')])
def update_graph(selected_state, xaxis_name, yaxis_name):
    filtered_df = df[df['State'] == selected_state]
    traces = []

    for county_name in filtered_df['County'].unique():
        df_by_county = filtered_df[filtered_df['County'] == county_name]
        traces.append(go.Scatter(
            x=df_by_county[xaxis_name],
            y=df_by_county[yaxis_name],
            text=df_by_county['County'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=county_name
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'linear', 'title': xaxis_name},
            yaxis={'title': yaxis_name},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server()
