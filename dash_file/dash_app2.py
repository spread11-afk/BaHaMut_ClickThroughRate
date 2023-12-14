from dash import Dash, html, dash_table, Input, Output, callback, dcc, State
import pandas as pd
import dash_bootstrap_components as dbc
import pandas as pd

dash2 = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
dash2.title = "台北市youbike及時資料"
df = pd.read_csv('BaHaMut_9.csv')
df1 = df.reset_index()
dash2.layout = html.Div(
    [
        dbc.Container([
            html.Div([
                html.Div([
                    html.H1("BaHaMutAnime")
                ], className="title")
            ],
                className="title-row",
                style={"paddingTop": '2rem'}),
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        id='main_table',
                        data=df1.to_dict('records'),
                        columns=[{'id': column, 'name': column}
                                 for column in df1.columns],
                        page_size=30,
                        # style_table={'height': '800px', 'overflowY': 'auto'},
                        fixed_rows={'headers': True},
                        row_selectable="single",
                        selected_rows=[]
                    ),
                ], className="main")
            ],
                className="main-row",
                style={"paddingTop": '2rem'}),
            html.Div([
                html.Div(className="col", id='showMessage')
            ],
                className="row",
                style={"paddingTop": '2rem'})

        ])
    ],
    className="container-lg"
)


@callback(
    Output('showMessage', 'children'),
    Input('main_table', 'selected_rows')
)
def selectedRow(selected_rows: list[int]):
    # 取得一個站點,series
    if len(selected_rows) != 0:
        print("執行")
        oneSite: pd.DataFrame = df1.iloc[[selected_rows[0]]]
        oneTable: dash_table.DataTable = dash_table.DataTable(
            oneSite.to_dict('records'), [{"name": i, "id": i} for i in oneSite.columns])
        return [oneTable]

    return None


if __name__ == "__main__":
    dash2.run(host='127.0.0.1', port=8050, debug=True)
