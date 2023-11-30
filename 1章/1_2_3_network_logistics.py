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


def draw_arc(G, pos, node1, node2, radius):
    theta1 = np.arctan2(pos[node2][1] - pos[node1][1],
                        pos[node2][0] - pos[node1][0])
    theta2 = np.arctan2(pos[node1][1] - pos[node2][1],
                        pos[node1][0] - pos[node2][0])

    start_pos = (pos[node1][0] + radius * np.cos(theta1),
                 pos[node1][1] + radius * np.sin(theta1))
    end_pos = (pos[node2][0] + radius * np.cos(theta2),
               pos[node2][1] + radius * np.sin(theta2))

    arc = plt.Arrow(
        start_pos[0], start_pos[1],
        end_pos[0] - start_pos[0], end_pos[1] - start_pos[1],
    )

    plt.gca().add_patch(arc)


def plot_network():

    data_df = pd.read_csv("matrix.csv", index_col=0)

    # 空の無向グラフを作成
    G = nx.DiGraph()
    data = np.log1p(data_df.values)
    # 対角要素をゼロにする
    np.fill_diagonal(data, 0)

    threshold = np.percentile(data, 95)
    prefec_list = list(data_df.index)
    for pref in prefec_list:
        G.add_node(prefecture_dictionary[pref])

    # グラフにエッジと重みを追加
    for i in range(len(data_df)):
        for j in range(len(data_df)):
            G.add_edge(prefecture_dictionary[prefec_list[i]], prefecture_dictionary[prefec_list[j]],
                       weight=data[i, j] * 0.1) if data[i, j] >= threshold else None

    # ノードの数に応じて、楕円上に等間隔でノードを配置
    nodes = G.nodes()
    theta = np.linspace(0 + 0.5 * np.pi, 2 * np.pi +
                        0.5 * np.pi, len(nodes) + 1)[:-1]
    a, b = 1, 1.5  # a, bはそれぞれ楕円の長軸と短軸の長さ
    pos = {node: (a * np.cos(angle), b * np.sin(angle))
           for node, angle in zip(nodes, theta)}

    # エッジの太さのリストを作成
    edge_widths = [G[u][v]['weight'] for u, v in G.edges()]
    min_weight = min(edge_widths)
    max_weight = max(edge_widths)

    # 図の作成
    fig, ax = plt.subplots(figsize=(10, 10))
    cmap = cm.get_cmap('jet')

    for edge in G.edges():
        source, target = edge
        rad = 0.5
        norm_weight = (G.edges[(source, target)]['weight'] -
                       min_weight) / (max_weight - min_weight)
        color = cmap(norm_weight)
        arrowprops = dict(lw=G.edges[(source, target)]['weight'],
                          arrowstyle="simple",
                          color=color,
                          connectionstyle=f"arc3,rad={rad}",
                          # linestyle='-',
                          alpha=0.5,
                          shrinkB=10,
                          shrinkA=10)
        ax.annotate("",
                    xy=pos[target],
                    xytext=pos[source],
                    arrowprops=arrowprops
                    )

    nx.draw_networkx_nodes(G, pos, node_color='black',
                           edgecolors='white', alpha=0.5, node_size=500)

    # ラベルを個別に描画
    for node in G.nodes():
        if len(node) == 2:
            nx.draw_networkx_labels(G, pos, labels={
                                    node: node}, font_color='white', font_size=10, font_family="IPAexGothic")
        else:
            nx.draw_networkx_labels(G, pos, labels={
                                    node: node}, font_color='white', font_size=7, font_family="IPAexGothic")

    plt.axis('off')  # 軸を非表示
    plt.gca().set_aspect('equal', adjustable='datalim')  # アスペクト比を調整
    plt.savefig("1_2_3_network_logistics.png", dpi=300)  # 画像として保存
    plt.show()  # 図を表示


if __name__ == "__main__":
    plot_network()
