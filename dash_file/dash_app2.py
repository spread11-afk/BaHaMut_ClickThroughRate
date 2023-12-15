from dash import Dash, html, dash_table, Input, Output, callback, dcc, State
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import pandas as pd
import base64


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
                    page_size=20,
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
            html.Div(className="showselect",
                     id='showMessage'), html.Img(src=dash.get_asset_url('史萊姆.png'))
        ],
            className="maincontainer",
            style={"paddingTop": '2rem'}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody([html.H1('123123')], id="modal-content"),
            ],
            id="modal",
            is_open=False,
        )


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


selected_row = None
page_current = 0


@callback(
    Output("modal-content", "children"),
    Output("modal", "is_open"),
    Input("main_table", "active_cell"),
    State("main_table", "page_current")
)
def update_graphs(active_cell, page_current):
    df.reset_index(drop=True, inplace=True)
    global selected_row
    # image_filename = r'assets/suraimu.png'
    # file = open(image_filename, 'rb')
    # encoded_image = base64.b64encode(file.read()).decode('ascii')
    # if active_cell and active_cell["column_id"] == "動畫名":
    if active_cell and active_cell["column_id"] == "動畫名":
        if page_current == None:
            page_current = 0
        selected_row = active_cell["row"] + page_current * 20
        info = df.loc[selected_row][active_cell["column_id"]]
    # cell_data = html.Img(src='../static/images/史萊姆.png')
        if info == "關於我轉生變成史萊姆這檔事 第二季":
            info = html.H1('關於我轉生變成史萊姆這檔事 第二季')
        return info, True
    return dash.no_update, False


if __name__ == "__main__":
    dash2.run(host='127.0.0.1', port=8050, debug=True)
