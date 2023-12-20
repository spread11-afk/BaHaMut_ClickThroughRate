import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, dash_table
import pandas as pd

df1 = pd.read_csv('genre_table.csv')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)
# html.Div([dcc.Location(id="url"), sidebar, content]),
app.layout = html.Div([
    html.H1(['影響觀看數因子'], style={'textAlign': 'center'}),
    dcc.Dropdown(['作品分類(全部)', '作品分類(代表性)', '原創改編、新續作'],'作品分類(全部)', id='dropdown_selection'),
    html.Div([dash_table.DataTable([],id='main_table')],className='main')],className='mycontainer')



@app.callback(
    Output("main", "main_table"),
    Input('mycontainer', 'dropdown_selection')
)
def dropdownSelection(dropdown_selection):
    if dropdown_selection == '作品分類(全部)':
        print(dropdown_selection)




# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname == "/":
        
        
#         return [html.Div([
#                 html.H1(children='影響觀看數因子', style={'textAlign':'center'}),
#                 dcc.Dropdown(['作品分類(全部)','作品分類(代表性)','原創改編、新續作'], '作品分類(全部)', id='dropdown-selection'),
#                 dash_table.DataTable(data=df1.to_dict('records'), page_size=10, id='main_table'),])]
    # elif pathname == "/page-1":
    #     return html.P("This is the content of page 1. Yay!")
    # elif pathname == "/page-2":
    #     return html.P("Oh cool, this is page 2!")
    # # If the user tries to reach a different page, return a 404 message
    # return html.Div(
    #     [
    #         html.H1("404: Not found", className="text-danger"),
    #         html.Hr(),
    #         html.P(f"The pathname {pathname} was not recognised..."),
    #     ],
    #     className="p-3 bg-light rounded-3",
    # )




if __name__ == "__main__":
    app.run_server(port=8888,debug=True)