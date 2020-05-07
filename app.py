import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px 

app = dash.Dash(__name__)
server=app.server

#app.layout = html.Div(
#    html.H1(children = 'Samu dash')
#    )

#df = pd.read_csv('samudata.csv')
gapminder = px.data.gapminder()

fig = px.scatter(gapminder, x=gapminder.gdpPercap, y='lifeExp', size='pop', color='country',
hover_name='country',
animation_frame='year', animation_group='country', size_max=50, log_x=True)

app.layout = html.Div(
    [
        html.H1(children = 'Gapminder dash'),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"},
        figure = fig)
        #px.scatter(df, df.comment, df.views, color=df.datetime.dt.year, log_x=True, log_y=True)
    ]
)
    
if __name__=='__main__':
    app.run_server(debug=True)
    
