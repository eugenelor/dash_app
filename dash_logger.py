import dash
import dash_core_components as dcc
import dash_html_components as html
import time
from collections import deque
import plotly.graph_objs as go
import random



max_length = 50
times = deque(maxlen=max_length)
sensorA = deque(maxlen=max_length)
sensorB = deque(maxlen=max_length)
sensorC = deque(maxlen=max_length)
sensorD = deque(maxlen=max_length)
sensorE = deque(maxlen=max_length)
sensorF = deque(maxlen=max_length)

data_dict = {"Sensor A":sensorA,
"Sensor B": sensorB,
"Sensor C": sensorC,
"Sensor D":sensorD,
"Sensor E":sensorE,
"Sensor F":sensorF}

def update_obd_values(times, sensorA, sensorB, sensorC, sensorD, sensorE, sensorF):
    times.append(time.time())
    if len(times) == 1:
                #starting relevant values
        sensorA.append(random.uniform(10,300000))
        sensorB.append(random.uniform(50,620000))
        sensorC.append(random.uniform(45,670000))
        sensorD.append(random.uniform(96,152000))
        sensorE.append(random.uniform(72,990000))
        sensorF.append(random.uniform(62,980000))
    else:
        for data_of_interest in [sensorA, sensorB, sensorC, sensorD, sensorE, sensorF]:
            data_of_interest.append(data_of_interest[-1]+data_of_interest[-1]*random.uniform(-0.0001,0.0001))

    return times, sensorA, sensorB, sensorC, sensorD, sensorE, sensorF

times, sensorA, sensorB, sensorC, sensorD, sensorE, sensorF = update_obd_values(times, sensorA, sensorB, sensorC, sensorD, sensorE, sensorF)

# Dashboard Body
external_css = ["https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css"]
external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']

app = dash.Dash('vehicle-data',
                external_scripts=external_js,
                external_stylesheets=external_css)
server = app.server

app.layout = html.Div([
    html.Div([
        html.H2('Sensor Data',
                style={'float': 'left'})
        ]),

    dcc.Dropdown(id='sensor-data-name',
                 options=[{'label': s, 'value': s}
                          for s in data_dict.keys()],
                 value=['Sensor A','Sensor B','Sensor C'],
                 multi=True
                 ),

    html.Div(children=html.Div(id='graphs'), className='row'),

    dcc.Interval(
        id='graph-update',
        interval=1000,
        n_intervals=0),
    ],

    className="container",style={
        'width':'98%','margin-left':10,'margin-right':10,'max-width':50000

        })



@app.callback(
    dash.dependencies.Output('graphs','children'),
    [dash.dependencies.Input('sensor-data-name', 'value'),
     dash.dependencies.Input('graph-update', 'n_intervals')],
    )

def update_graph(data_names, n):
    graphs = []
    update_obd_values(times, sensorA, sensorB, sensorC, sensorD, sensorE, sensorF)
    if len(data_names)>2:
        class_choice = 'col s12 m6 l4'
    elif len(data_names) == 2:
        class_choice = 'col s12 m6 l6'
    else:
        class_choice = 'col s12'

    for data_name in data_names:
        data = go.Scatter(
            x=list(times),
            y=list(data_dict[data_name]),
            name='Scatter',
            fill="tozeroy",
            fillcolor="#6897bb"
            )

        graphs.append(html.Div(dcc.Graph(
            id=data_name,
            animate=True,
            figure={'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
                                                        yaxis=dict(range=[min(data_dict[data_name]),max(data_dict[data_name])]),
                                                        margin={'l':50,'r':1,'t':45,'b':1},
                                                        title='{}'.format(data_name))}), className=class_choice))

    return graphs



if __name__ == '__main__':
    app.run_server(debug=True)
