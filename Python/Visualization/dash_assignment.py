from dash import Dash, html, dcc, callback, dash_table, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
df_subset = df.head(5)

# Creating the app instance
app = Dash(__name__)

#creating the layout
app.layout = html.Div([
                        #graph
                        html.H1(children='Population Graph', style={'textAlign':'center'}),#header with title and css styling
                        dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection-country'),
                        dcc.Graph(id='graph-content'),
                        
                        # table
                        html.H1(children='Population Table', style={'textAlign':'center'}),
                        dcc.Dropdown(df.year.unique(), 1950 , id='dropdown-selection-year'),
                        dash_table.DataTable(
                            id = "table",
                            columns=[{"name": i, "id": i} for i in df_subset.columns],
                            data=df.to_dict('records'),
                        )
                        ])
            

# Graph call Back
@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection-country', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

# Define the callback function
@app.callback(
    Output('table', 'data'),
    [Input('table', 'filter_query')]
)
def update_table(filter_query):
    dff = df[df["year"]==filter_query]
    return dff.to_dict('records')


if __name__ == '__main__':
    app.run(debug=True)