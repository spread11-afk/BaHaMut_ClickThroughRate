from dash import Dash, html, dash_table, Input, Output, callback, dcc, State
import pandas as pd
import dash_bootstrap_components as dbc
import pandas as pd

dash2 = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
dash2.title = "BaHaMutAnime"
df = pd.read_csv('BaHaMut_9.csv')
dash2.layout = html.Div(
    [

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
                    data=df.to_dict('records'),
                    columns=[{'id': column, 'name': column}
                             for column in df.columns],
                    sort_action='native',  # 启用原生排序功能
                    sort_mode='multi',
                    style_cell={'whiteSpace': 'normal', 'textAlign': 'center'},
                    style_cell_conditional=[
                        {'if': {'column_id': '動畫名'}, 'width': '190px'}, {'if': {'column_id': '年份'}, 'width': '75px'}, {'if': {'column_id': '月份'}, 'width': '75px'}, {'if': {'column_id': '集數'}, 'width': '75px'}, {'if': {'column_id': '星級'}, 'width': '75px'}, {'if': {'column_id': '評分人數'}, 'width': '50px'}, {'if': {'column_id': '導演監督'}, 'width': '80px'}, {'if': {'column_id': '製作廠商'}, 'width': '85px'}, {'if': {'column_id': '作品分類1'}, 'width': '50px'}, {'if': {'column_id': '作品分類2'}, 'width': '50px'}, {'if': {'column_id': '作品分類3'}, 'width': '50px'}, {'if': {'column_id': '作品分類4'}, 'width': '50px'}, {'if': {'column_id': '作品分類5'}, 'width': '50px'}, {'if': {'column_id': '作品分類6'}, 'width': '50px'}, {'if': {'column_id': '原作載體'}, 'width': '50px'}, {'if': {'column_id': '新續作'}, 'width': '65px'}, {'if': {'column_id': '平均觀看數(萬)'}, 'width': '75px'}, {'if': {'column_id': '總觀看數(萬)'}, 'width': '75px'}],
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
            html.Div(className="showselect", id='showMessage')
        ],
            className="maincontainer",
            style={"paddingTop": '2rem'})


    ],
    className="mycontainer"
)


@callback(
    Output('showMessage', 'children'),
    Input('main_table', 'selected_rows')
)
def selectedRow(selected_rows: list[int]):
    # 取得一個站點,series
    if len(selected_rows) != 0:
        print("執行")
        oneSite: pd.DataFrame = df.iloc[[selected_rows[0]]]
        oneTable: dash_table.DataTable = dash_table.DataTable(
            oneSite.to_dict('records'), [{"name": i, "id": i} for i in oneSite.columns], style_cell={'whiteSpace': 'normal', 'textAlign': 'center'})
        return [oneTable]

    return None


if __name__ == "__main__":
    dash2.run(host='127.0.0.1', port=8050, debug=True)
