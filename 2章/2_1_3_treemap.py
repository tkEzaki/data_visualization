import plotly.express as px  # tree map を利用するためのライブラリ
import numpy as np  # 数値計算のためのライブラリ
# import kaleido  # plotlyで画像を保存するためのライブラリ、追加でpip installが必要な場合がある


df = px.data.gapminder().query("year == 2007")  # gapminderデータセットから2007年のデータを抽出
fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                 color='lifeExp', hover_data=['iso_alpha'],
                 color_continuous_scale='RdBu',
                 color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))  # マージンの設定
fig.write_image("2_1_3_treemap_test.png")  # 画像として保存
