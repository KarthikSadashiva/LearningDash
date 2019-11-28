import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import math
import numpy as np
from dash.dependencies import Input, Output
import random
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div([
        html.H1('Logarithmic Function Generator'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=0.2*1000, # in milliseconds
            n_intervals=0
        )
    ])
)
x = 1
X = []
Y = []

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    global x
    y = math.log(x, math.e) #random.randint(270, 300) #y = 3*math.pow(x, 3) - 5*math.pow(x, 2) + 7*x - 9
    x += 1

    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('X: {} Y: {}'.format(x, y), style=style)
    ]


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph(n):
    global x
    global X
    global Y
    X.append(x)
    y = math.log(x, math.e) #random.randint(270,300) #y = 3 * math.pow(x, 3) - 5 * math.pow(x, 2) + 7 * x - 9
    Y.append(y)
    print(x, y)
    trace = go.Scatter(
        x=X,
        y=Y,
        name='Scatter',
        mode='lines+markers'
    )
    return {'data': [trace],
            'layout': go.Layout(
                title='Log to base e',
                xaxis_title='x',
                yaxis_title='f(x) = ln(x)',
                showlegend=True,
                xaxis=dict(range=[0, len(X)]),
                yaxis=dict(range=[min(Y)*0.5, max(Y)*1.5])),
            }


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8051, debug=True)
