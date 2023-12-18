from dash import Dash, html, dash_table, Input, Output, callback, dcc, State
import dash
import pandas as pd
import dash_bootstrap_components as dbc
import pandas as pd
import base64


image_filename = './assets/suraimu.png'


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64decode(image).decode('utf-8')


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
                     id='showMessage'),
            html.Img(src=(
                './assets/images/attack.png'))
        ],
            className="maincontainer",
            style={"paddingTop": '2rem'}),
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody([html.H1('123123')], id="modal-content"),
            ],
            id="modal",
            className='modalsize',
            is_open=False,
            size='lg'
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
    Output("modal", "children"),
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
        info = dbc.ModalHeader(dbc.ModalTitle("關於我轉生變成史萊姆這檔事 第二季"),class_name='infotitle'), html.Div([html.Img(src='assets/suraimu.png'),
                                                                              html.P('三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！ STAFF 原作：川上泰樹、伏瀨、みっ')],className='info')
        return info, True
    return dash.no_update, False


if __name__ == "__main__":
    dash2.run(host='127.0.0.1', port=8050, debug=True)
