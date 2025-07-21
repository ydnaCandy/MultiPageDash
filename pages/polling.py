import dash
from dash import html, dcc

dash.register_page(__name__, path="/polling", name="定期更新")

layout = html.Div([
    html.H3("定期更新ページ"),
    dcc.Interval(id="interval", interval=5000, n_intervals=0),
    dcc.Graph(id="polling-graph")
])

# 必要ならこのファイルにcallbackも追加してOK
