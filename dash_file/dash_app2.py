from dash import Dash, html, dash_table, Input, Output, callback, dcc, State
import pandas as pd
import dash_bootstrap_components as dbc
import pandas as pd

dash2 = Dash(requests_pathname_prefix="/dash/app2/",
             external_stylesheets=[dbc.themes.BOOTSTRAP])
dash2.title = "台北市youbike及時資料"
df = pd.read_csv('BaHaMut_9.csv')

# lastest_df = pd.DataFrame(lastest_data,columns=['站點名稱','更新時間','行政區','地址','總數','可借','可還'])
df1 = df.reset_index()

dash2.layout = html.Div(
    [
        dbc.Container([
            html.Div([
                html.Div([
                    html.H1("BaHaMutAnime")
                ], className="col text-center")
            ],
                className="row",
                style={"paddingTop": '2rem'}),
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        id='main_table',
                        data=df1.to_dict('records'),
                        columns=[{'id': column, 'name': column}
                                 for column in df1.columns],
                        page_size=20,
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        fixed_rows={'headers': True},
                        style_cell_conditional=[
                            {'if': {'column_id': 'index'},
                             'width': '5%'
                             },
                            {'if': {'column_id': '站點名稱'},
                             'width': '25%'},
                            {'if': {'column_id': '總數'},
                             'width': '5%'},
                            {'if': {'column_id': '可借'},
                             'width': '5%'},
                            {'if': {'column_id': '可還'},
                             'width': '5%'},
                        ],
                        row_selectable="single",
                        selected_rows=[]
                    ),
                ], className="col text-center")
            ],
                className="row",
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
