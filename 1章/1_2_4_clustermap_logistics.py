import pandas as pd  # データフレーム操作のためのPandas
import seaborn as sns  # グラフ作成のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
import networkx as nx  # グラフ理論のためのNetworkX
from networkx.drawing.nx_pydot import graphviz_layout  # グラフのレイアウト指定のため
import matplotlib.cm as cm  # カラーマップのためのMatplotlib
import matplotlib as mpl  # Matplotlibの設定
import ast  # Pythonのリストや辞書の文字列を変換するため
from matplotlib import font_manager  # フォント管理のためのMatplotlib
import matplotlib.patches as patches  # 図形描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ


plt.rcParams['font.size'] = 14


prefecture_dictionary = {
    'Hokkaido': '北海道',
    'Aomori': '青森',
    'Iwate': '岩手',
    'Miyagi': '宮城',
    'Akita': '秋田',
    'Yamagata': '山形',
    'Fukushima': '福島',
    'Ibaraki': '茨城',
    'Tochigi': '栃木',
    'Gunma': '群馬',
    'Saitama': '埼玉',
    'Chiba': '千葉',
    'Tokyo': '東京',
    'Kanagawa': '神奈川',
    'Niigata': '新潟',
    'Toyama': '富山',
    'Ishikawa': '石川',
    'Fukui': '福井',
    'Yamanashi': '山梨',
    'Nagano': '長野',
    'Gifu': '岐阜',
    'Shizuoka': '静岡',
    'Aichi': '愛知',
    'Mie': '三重',
    'Shiga': '滋賀',
    'Kyoto': '京都',
    'Osaka': '大阪',
    'Hyogo': '兵庫',
    'Nara': '奈良',
    'Wakayama': '和歌山',
    'Tottori': '鳥取',
    'Shimane': '島根',
    'Okayama': '岡山',
    'Hiroshima': '広島',
    'Yamaguchi': '山口',
    'Tokushima': '徳島',
    'Kagawa': '香川',
    'Ehime': '愛媛',
    'Kochi': '高知',
    'Fukuoka': '福岡',
    'Saga': '佐賀',
    'Nagasaki': '長崎',
    'Kumamoto': '熊本',
    'Oita': '大分',
    'Miyazaki': '宮崎',
    'Kagoshima': '鹿児島',
    'Okinawa': '沖縄'
}

# 都道府のラベル
prefectures_name = np.array(["北海道", "青森", "岩手", "宮城", "秋田",
                             "山形", "福島", "茨城", "栃木", "群馬",
                             "埼玉", "千葉", "東京", "神奈川", "新潟",
                             "富山", "石川", "福井", "山梨", "長野",
                             "岐阜", "静岡", "愛知", "三重", "滋賀",
                             "京都", "大阪", "兵庫", "奈良", "和歌山",
                             "鳥取", "島根", "岡山", "広島", "山口",
                             "徳島", "香川", "愛媛", "高知", "福岡",
                             "佐賀", "長崎", "熊本", "大分", "宮崎", "鹿児島", "沖縄"])
# 経度x(沖縄を0地点に変換)
prefectures_x = np.array([13.666967, 13.059661, 13.471735, 13.191171, 12.421402,
                          12.682702, 12.786589, 12.765861, 12.202633, 11.379224,
                          11.968001, 12.442376, 12.010772, 11.961582, 11.342289,
                          9.530406, 8.944641, 8.54071, 10.887517, 10.500292,
                          9.041359, 10.702122, 9.225633, 8.827659, 8.187658,
                          8.074676, 7.838779, 7.502093, 8.151812, 7.486574,
                          6.55674, 5.369567, 6.253743, 4.77869, 3.789568,
                          6.878371, 6.362512, 5.08443, 5.850148, 2.737382,
                          2.61789, 2.192824, 3.060735, 3.931659, 3.742923, 2.877049, 0])
# 緯度y(沖縄を0地点に変換)
prefectures_y = np.array([16.851567, 14.612222, 13.49113, 12.056438, 13.506199,
                          12.028036, 11.537898, 10.129412, 10.353324, 10.178807,
                          9.645027, 9.392657, 9.47712, 9.235352, 11.690017,
                          10.482889, 10.382281, 9.852818, 9.451757, 10.438888,
                          9.178826, 8.764577, 8.967787, 8.517882, 8.79213,
                          8.808603, 8.473915, 8.478878, 8.472932, 8.013633,
                          9.291468, 9.259896, 8.449371, 8.184159, 7.97372,
                          7.853369, 8.127748, 7.629259, 7.347304, 7.394384,
                          7.036966, 6.532438, 6.577427, 7.025793, 5.698689, 5.347747, 0])

pref_pos_dict = dict(zip(prefectures_name, zip(prefectures_x, prefectures_y)))


def plot_cluster_map():
    # CSVファイルからデータを読み込む
    data_df = pd.read_csv("matrix.csv", index_col=0)

    # 都道府県名を英日対応辞書(prefecture_dictionary)を使用して日本語に変換
    data_df.index = [prefecture_dictionary[pref] for pref in data_df.index]
    data_df.columns = [prefecture_dictionary[pref] for pref in data_df.columns]

    # データに対数変換（log1p）を適用
    data_df = np.log1p(data_df)

    # Seabornを使用してクラスターマップを作成し、図を取得
    g = sns.clustermap(data_df, cmap="jet", metric='euclidean',
                       method='ward', figsize=(12, 12))

    plt.setp(g.ax_heatmap.xaxis.get_majorticklabels(),
             rotation=90)  # X軸の軸ラベルを90度回転して表示
    plt.setp(g.ax_heatmap.yaxis.get_majorticklabels(),
             rotation=0)  # Y軸の軸ラベルを0度で表示

    # X軸とY軸の目盛りを調整してすべて表示
    g.ax_heatmap.set_xticks(np.arange(len(data_df.columns)) + 0.5)
    g.ax_heatmap.set_yticks(np.arange(len(data_df.index)) + 0.5)

    # X軸とY軸の目盛りに都道府県名を設定
    g.ax_heatmap.set_xticklabels(data_df.columns)
    g.ax_heatmap.set_yticklabels(data_df.index)

    plt.savefig("1_2_4_clustermap_logistics.png", dpi=300)  # 画像を保存
    plt.show()  # 画像を表示


if __name__ == "__main__":
    plot_cluster_map()
