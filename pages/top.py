import dash
from dash import html, dcc

dash.register_page(__name__, path="/", name="Topページ")

layout = html.Div([
    html.H3("トップページ"),
    dcc.Graph(id="realtime-graph"),
    # WebSocket追加するならここ
])
