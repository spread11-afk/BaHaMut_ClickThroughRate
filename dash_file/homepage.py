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
dash2.layout = html.Div([html.Div([html.Div(['AnimeTrailer'], className='trailer'), html.Div(
    [html.Video(src='assets/movies/葬送のフリーレン.mp4', autoPlay=True, muted=True, loop=True, width='100%', height='100%')], className='movie')], className='moviebox')], className="mycontainer1")


if __name__ == "__main__":
    dash2.run(host='127.0.0.1', port=8050, debug=True)
