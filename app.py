import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px 

app = dash.Dash(__name__)

#app.layout = html.Div(
#    html.H1(children = 'Samu dash')
#    )

df = pd.read_csv('https://archive.org/download/samudata/samudata.csv')




app.layout = html.Div(
    [
        html.H1(children = 'Samu dash'),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"},
        figure = px.histogram(df, df.datetime, color=df.datetime.dt.year, hover_name=df.datetime.dt.date))
        #px.scatter(df, df.comment, df.views, color=df.datetime.dt.year, log_x=True, log_y=True)
    ]
)
    
if __name__=='__main__':
    app.run_server(debug=True)
    
