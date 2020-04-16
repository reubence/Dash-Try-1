import pandas_datareader.data as web
import datetime
import os
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

start = datetime.datetime(2015,1,1)
end = datetime.datetime.now()
#     ALPHAVANTAGE_API_KEY = "QNIWSTJYOJM8EDNL"
df1 = web.DataReader('AAPL', 'yahoo', start, end)

app = dash.Dash()


app.layout = html.Div(children = [
    html.Div('''
        symbol to graph:
    '''),
    dcc.Input(id = 'input', type = 'text', placeholder = 'Enter Symbol Eg: yahoo', value = ''),
    html.Div(id = 'output-graph'),
])

@app.callback(
    Output(component_id='output-graph',component_property='children'),
    [Input(component_id='input',component_property='value')]
)
def update_graph(input_data):
    start = datetime.datetime(2015,1,1)
    end = datetime.datetime.now()
#     ALPHAVANTAGE_API_KEY = "QNIWSTJYOJM8EDNL"
    df1 = web.DataReader(input_data, 'yahoo', start, end)
    return dcc.Graph(id = 'example',
             figure = {
                 'data' :[{'x':df1.index, 'y': df1.Close, 'type': 'line', 'name':'stock'}],
                 'layout' :{'title':'Stock'}
             })
if __name__ == '__main__':
    app.run_server(debug=True)

