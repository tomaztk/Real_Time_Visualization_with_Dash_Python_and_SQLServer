"""
Author: Tomaz Kastrun
Date: 17.06.2018

Visualizing real-time data stream  using Python Dash and Microsoft SQL Server


"""

import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
from collections import deque
import pandas as pd
import pyodbc


def connectSQLServer(driver, server, db):
    connSQLServer = pyodbc.connect(
        r'DRIVER={' + driver + '};'
        r'SERVER=' + server + ';'
        r'DATABASE=' + db + ';'
        r'Trusted_Connection=yes;',
        autocommit=True
    )
    return connSQLServer 


name_title = 'Stats from SQL Server'
app = dash.Dash(__name__)

app.layout = html.Div(children=[
        
    html.H1(children='Read near real-time data from SQL Server on Scatterplot '),
     dcc.Graph(
        id='example-graph',animate=True),dcc.Interval(id='graph-update',interval=1*500),])

    
@app.callback(Output('example-graph', 'figure'), 
              events=[Event('graph-update', 'interval')])


def update_graph_scatter():

    dataSQL = [] #set an empty list
    X = deque(maxlen=10)    
    Y = deque(maxlen=10)

    sql_conn = connectSQLServer('ODBC Driver 13 for SQL Server', 'TOMAZK\MSSQLSERVER2017', 'test') 
    cursor = sql_conn.cursor()
    cursor.execute("SELECT num,ID FROM dbo.LiveStatsFromSQLServer")
    rows = cursor.fetchall()
    for row in rows:
        dataSQL.append(list(row))
        labels = ['num','id']
        df = pd.DataFrame.from_records(dataSQL, columns=labels)
        X = df['id']
        Y = df['num']
        

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}

if __name__ == "__main__":
    app.run_server(debug=True)