import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# ====================================================================
# 補足
# assetsフォルダのcssでbodyタグのmarginとpaddingを0にしています。
# ====================================================================

# =================================================================
# インスタンスの生成
# =================================================================
app = Dash(__name__, use_pages=True)

# gunicorn用
server = app.server

# =================================================================
# メインページのレイアウト定義
# =================================================================

app.layout = html.Div(
    [
        # サイドバー
        html.Div(
            [
                html.Div(
                    [
                        html.H2('My Dashboard'),
                    ],style={
                        'color': 'white'
                    }
                ),
                html.Div(
                    [
                        html.Div(
                            # pagesディレクトリ内のpyファイルを表示
                            dcc.Link(f"{page['name']}", href=page["relative_path"],style={"color": "white"}),
                        ) for page in dash.page_registry.values()
                    ]
                ),
            ],style={
                'width': '15%',                    # サイドバーの幅
                "height": "100%",
                "margin": '0px',
                "background": "#203A5E",
                'display': 'inline-block',         # サイドバーレイアウトの定義
                'vertical-align': 'top',           # 上端揃え
                'border-right': '1px solid #ccc',  # 右端の境界線を定義
            }
        ),
        # メインコンテンツ
        html.Div(
            # タイトル
            [
                dash.page_container,               # サイドバーで選択されたページのコンテンツを表示
            ],style={
                'width': '84%',                    # メインコンテンツの幅。サイドバーと合わせて100%を超えるとレイアウトが崩れる
                'display': 'inline-block',         # サイドバーレイアウトの定義
                "background": "#F6F7FB",
                "height": "100%",
                "margin": '0px',
            }
        ),
    ],style={
        "width": "100vw",
        "height": "100vh",
        "margin": '0',
        'padding': '0',
        'color': '#464647'
    }
)

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)