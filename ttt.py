import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import nsetools
import time

app = dash.Dash(__name__)

app.layout = html.Div(
    html.Div([
        html.H1('NSE Live Chart - TCS'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=5*1000, # in milliseconds
            n_intervals=0
        )
    ])
)
x = time.strftime("%H:%M:%S", time.localtime())
X = []
Y = []
nse = nsetools.Nse()

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    global x
    y = nse.get_quote('TCS')["lastPrice"]
    # y = nsepy.live.get_quote('PNB')['lastPrice']
    #y = math.log(x, math.e) #random.randint(270, 300) #y = 3*math.pow(x, 3) - 5*math.pow(x, 2) + 7*x - 9
    x = time.strftime("%H:%M:%S", time.localtime())

    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Time: {} TCS: {}'.format(x, y), style=style)
    ]


@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph(n):
    global x
    global Y
    x = time.strftime("%H:%M:%S", time.localtime())
    X.append(x)
    y = nse.get_quote('TCS')["lastPrice"]
    # y = nsepy.live.get_quote('PNB')['lastPrice']

    # y = math.log(x, math.e) #random.randint(270,300) #y = 3 * math.pow(x, 3) - 5 * math.pow(x, 2) + 7 * x - 9
    Y.append(y)
    # print(x, y)
    trace = go.Scatter(
        x=X,
        y=Y,
        name='TCS',
        mode='lines',
        fill='tozeroy',
        gradient=True
    )
    return {'data': [trace],
            'layout': go.Layout(
                title='TCS - 28th November 2019',
                xaxis_title='Time',
                yaxis_title='Share Price in Rs.',
                xaxis=dict(range=[0, len(X)]),
                showlegend=True,
                yaxis=dict(range=[min(Y)-10, max(Y)+10]))
            }


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8053, debug=True)
