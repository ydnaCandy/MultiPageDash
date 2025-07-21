from dash import Dash, html, dcc, page_container
import dash_bootstrap_components as dbc



app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "プリザンダーダッシュボード"

app.layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col([
            html.H2("メニュー", className="mt-3"),
            dbc.Nav([
                dbc.NavLink("Topページ", href="/", active="exact"),
                dbc.NavLink("定期更新ページ", href="/polling", active="exact"),
                dbc.NavLink("リアルタイムページ", href="/realtime", active="exact"),
            ], vertical=True, pills=True),
        ], width=2, style={"backgroundColor": "#f8f9fa", "height": "100vh"}),

        dbc.Col([
            page_container  # register_pageしたページがここに表示される
        ], width=10)
    ])
])

if __name__ == "__main__":
    app.run(debug=True)