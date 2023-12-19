import dash
from dash import Dash, html, dash_table, Input, Output, callback, dcc, State
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
                html.Div([
                    dbc.Input(id='input_value',
                              placeholder="請輸入動畫名稱", type="text"),
                ])
            ], className="col"),
            html.Div([
                html.Button('確定', id='submit-val', className="btn btn-primary")
            ], className="col")
        ],
            className="row row-cols-auto align-items-end",
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
                    style_cell={'whiteSpace': 'normal',
                                'textAlign': 'center'},
                    style_cell_conditional=[
                        {'if': {'column_id': '動畫名'}, 'width': '190px'}, {'if': {'column_id': '年份'}, 'width': '75px'}, {'if': {'column_id': '月份'}, 'width': '75px'}, {'if': {'column_id': '集數'}, 'width': '75px'}, {'if': {'column_id': '星級'}, 'width': '75px'}, {'if': {'column_id': '評分人數'}, 'width': '50px'}, {'if': {'column_id': '導演監督'}, 'width': '80px'}, {'if': {'column_id': '製作廠商'}, 'width': '85px'}, {'if': {'column_id': '作品分類1'}, 'width': '50px'}, {'if': {'column_id': '作品分類2'}, 'width': '50px'}, {'if': {'column_id': '作品分類3'}, 'width': '50px'}, {'if': {'column_id': '作品分類4'}, 'width': '50px'}, {'if': {'column_id': '作品分類5'}, 'width': '50px'}, {'if': {'column_id': '作品分類6'}, 'width': '50px'}, {'if': {'column_id': '原作載體'}, 'width': '50px'}, {'if': {'column_id': '新續作'}, 'width': '65px'}, {'if': {'column_id': '平均觀看數(萬)'}, 'width': '75px'}, {'if': {'column_id': '總觀看數(萬)'}, 'width': '75px'}, {'backgroundColor': '#000'}, {'color': 'white'}],
                    page_size=20,
                    # style_table={'height': '800px', 'overflowY': 'hidden'},
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
                     id='showMessage')
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
    # Output('showMessage', 'children'),
    Output("modal", "children"),
    Output("modal", "is_open"),
    Input('main_table', 'selected_rows')
)
def selectedRow(selected_rows):
    if len(selected_rows) != 0:
        print(df.iloc[selected_rows[0]][0])
        oneSite: pd.DataFrame = df.iloc[[selected_rows[0]]],
        oneSite = oneSite[0]
        # oneTable: dash_table.DataTable = dash_table.DataTable(
        #     oneSite.to_dict('records'), [{"name": i, "id": i} for i in oneSite.columns], style_cell={'whiteSpace': 'normal', 'textAlign': 'center'})
        # for i in oneSite:
        #     print(i)
        # print(type(oneSite))
        # print(oneSite)
        # print(df.iloc[active_cell["row"], df.columns.get_loc(active_cell["column_id"])])
        if df.iloc[selected_rows[0]][0] == '關於我轉生變成史萊姆這檔事 第二季':
            info = html.Div([html.Div(html.A([html.Img(src='assets/suraimu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=20530", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        elif df.iloc[selected_rows[0]][0] == '咒術迴戰':
            info = html.Div([html.Div(html.A([html.Img(src='assets/jujutsu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=18626", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['虎杖悠仁是一位體育萬能的高中生，某天他為了從「咒物」危機中解救學長姊，而吞下了詛咒的手指，讓「宿儺」這種詛咒跟自己合而為一。之後他加入了專門培養咒術師的學校「咒術高專」，並遇到了伏黑惠與釘崎野薔薇這兩位同學。某日，突然出現「特級咒物」，他們三人就奉命到現場支援。為了實現爺爺要他「助人」的遺言，虎杖將會繼續與「詛咒」奮鬥下去。'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        # elif df.iloc[selected_rows[0]][0] == 'SPY×FAMILY 間諜家家酒':
            info = html.Div([html.Div(html.A([html.Img(src='assets/suraimu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=20530", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        # elif df.iloc[selected_rows[0]][0] == '進擊的巨人 The Final Season':
            info = html.Div([html.Div(html.A([html.Img(src='assets/suraimu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=20530", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        # elif df.iloc[selected_rows[0]][0] == '無職轉生，到了異世界就拿出真本事':
            info = html.Div([html.Div(html.A([html.Img(src='assets/suraimu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=20530", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        # elif df.iloc[selected_rows[0]][0] == 'Re：從零開始的異世界生活 第二季':
            info = html.Div([html.Div(html.A([html.Img(src='assets/suraimu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=20530", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        # elif df.iloc[selected_rows[0]][0] == '86－不存在的戰區－':
            info = html.Div([html.Div(html.A([html.Img(src='assets/suraimu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=20530", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        # elif df.iloc[selected_rows[0]][0] == '鬼滅之刃 遊郭篇':
            info = html.Div([html.Div(html.A([html.Img(src='assets/suraimu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=20530", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        # elif df.iloc[selected_rows[0]][0] == '輝夜姬想讓人告白～天才們的戀愛頭腦戰～ 第二季':
            info = html.Div([html.Div(html.A([html.Img(src='assets/suraimu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=20530", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        # elif df.iloc[selected_rows[0]][0] == '機動戰士鋼彈 水星的魔女 Season 2':
            info = html.Div([html.Div(html.A([html.Img(src='assets/suraimu_waifu2x_art_noise1_scale.png')], href="https://ani.gamer.com.tw/animeVideo.php?sn=20530", target="_blank"), className='infoimage'), html.Div([html.H1([df.iloc[selected_rows[0]][0]], style={'color': 'rgba(255, 208, 0, 0.89'}), html.H3([f'監督：{df.iloc[selected_rows[0]][6]}'], style={'color': 'rgba(0, 238, 255, 0.842', 'marginTop': '25px'}), html.H3([f'製作公司：{df.iloc[selected_rows[0]][7]}'], style={'color': 'rgba(0, 238, 255, 0.842'}),
                             html.H3(['三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！'], style={'marginTop': '25px', 'color': 'white'})], style={'padding': '15px'})], className='info')
        else:
            info = dbc.ModalHeader(dbc.ModalTitle(
                "尚未更新資料"), class_name='infotitle')
        return info, True
        # return [oneTable]
    return None, False


# @callback(
#     [Output('main_table', 'data'), Output('main_table', 'columns'),
#      Output('main_table', 'selected_rows')],
#     [Input('submit-val', 'n_clicks')],
#     [State('input_value', 'value')]
# )
# def clickBtn(n_clicks: None | int, inputValue: str):
#     global df
#     if n_clicks is not None:
#         # 一定先檢查有沒有按button
#         dff = df[df['動畫名'] == inputValue]
#         print(dff.to_dict('records'), [
#               {'id': column, 'name': column} for column in dff.columns])
#         return dff.to_dict('records'), [{'id': column, 'name': column} for column in dff.columns], []

#     n_clicks is None
#     # 代表第一次啟動
#     print("第一次啟動")
#     dff = df[df['動畫名'] == inputValue]
#     print("按確定")
#     return dff.to_dict('records'), [{'id': column, 'name': column} for column in df.columns], []


selected_row = None
page_current = 0


# @callback(
#     Output("modal", "children"),
#     Output("modal", "is_open"),
#     Input("main_table", "active_cell"),
#     State("main_table", "page_current")
# )
# def update_graphs(active_cell, page_current):
#     df.reset_index(drop=True, inplace=True)
#     global selected_row
#     # image_filename = r'assets/suraimu.png'
#     # file = open(image_filename, 'rb')
#     # encoded_image = base64.b64encode(file.read()).decode('ascii')
#     # if active_cell and active_cell["column_id"] == "動畫名":
#     if active_cell and active_cell["column_id"] == "動畫名":
#         if page_current == None:
#             page_current = 0
#         selected_row = active_cell["row"] + page_current * 20
#         info = dbc.ModalHeader(dbc.ModalTitle("關於我轉生變成史萊姆這檔事 第二季"),class_name='infotitle'), html.Div([html.Img(src='assets/suraimu.png'),
#                                                                               html.P('三上悟過著不起眼的人生，在隨機殺人魔肆虐下結束了三十七年生涯…… 看似如此。當他甦醒時，不僅眼睛看不見，就連耳朵也聽不到…… 面對一連串突發狀況，他意識到自己投胎轉世成「史萊姆」！儘管變成最弱魔物讓他頗有怨言，三上悟還是決定要快樂地過史萊姆生活，沒想到卻碰上天災級魔物「暴風龍維爾德拉」，命運就此出現巨大轉折──維爾德拉將他命名為「利姆路」，正要展開史萊姆式的異世界新生活時，卻被捲入哥布靈對牙狼族的紛爭之中，最後還莫名其妙當上魔物大王…… 能奪取對手能力的「捕食者」以及精通世界真理的「大賢者」，有這兩項特殊技能當武器，最強的史萊姆傳說正式展開！ STAFF 原作：川上泰樹、伏瀨、みっ')],className='info')
#         return info, True
#     return dash.no_update, False


if __name__ == "__main__":
    dash2.run(host='127.0.0.1', port=8050, debug=True)
