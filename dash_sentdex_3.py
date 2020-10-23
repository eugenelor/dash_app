import datetime
import yfinance as yf
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Stock Counter'),
    html.Div(children='''
        Symbol to graph
    '''),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')
])


@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    start=datetime.datetime(2017,1,1)
    end = datetime.datetime.now()
    df = yf.download(input_data, start=start,end=end)
    print (df.head())
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)

    return dcc.Graph(
        id='stock-graph',
        figure={
            'data':[
                {'x': df.index, 'y': df.Close, 'type':'line', 'name': input_data}
            ],
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server(debug=False)

# app = dash.Dash()
#
# app.layout = html.Div(children=
#     html.H1(children = 'TSLA Stock'))
# df = web.DataReader("TSLA", 'quandl', start, end)
# df.reset_index(inplace=True)
# df.set_index("Date", inplace=True)
# df = df.drop("Symbol", axis=1)
