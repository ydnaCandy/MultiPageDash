import dash
from dash import html, dcc

dash.register_page(__name__, path="/realtime", name="リアルタイム")

layout = html.Div([
    html.H3("リアルタイムページ"),
    dcc.Graph(id="realtime-graph"),
    # WebSocket追加するならここ
])
