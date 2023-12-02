import matplotlib.pyplot as plt  # Matplotlibのプロット機能を利用するためのライブラリをインポート
import japanize_matplotlib  # Matplotlibで日本語をサポートするためのライブラリをインポート
import numpy as np  # 数値計算のためのライブラリをインポート
import pandas as pd  # データ操作のためのライブラリをインポート

plt.rcParams["font.size"] = 14

# 棒グラフを描画する関数
def draw_bar_graph(prefectures, shipment):
    plt.figure(figsize=(12, 4))  # 図の設定
    plt.bar(prefectures, shipment, width=0.5)  # 棒グラフを描画
    plt.xticks(rotation=90)  # X軸のラベルを回転して表示
    plt.xlim(-0.5, 46.5)  # X軸の範囲を設定
    plt.tight_layout()  # レイアウトを調整
    plt.savefig("1_2_6_logistics_bar.png", dpi=300)  # 画像を保存
    plt.show()  # グラフを表示


def draw_sorted_bar_graph(prefectures, shipment):
    # 出荷量を降順にソートするためのインデックスを生成
    sorted_index = sorted(range(len(shipment)), key=lambda k: shipment[k], reverse=True)
    # インデックスを使って都道府県と出荷量をソート
    sorted_prefecture = [prefectures[i] for i in sorted_index]
    sorted_shipment = [shipment[i] for i in sorted_index]

    plt.figure(figsize=(12, 4))  # 図の設定
    plt.bar(sorted_prefecture, sorted_shipment, width=0.5)  # 棒グラフを描画
    plt.xticks(rotation=90)  # X軸のラベルを回転して表示
    plt.xlim(-0.5, 46.5)  # X軸の範囲を設定
    plt.tight_layout()  # レイアウトを調整
    plt.savefig("1_2_6_logistics_bar_sorted.png", dpi=300) # 画像を保存
    plt.show()  # グラフを表示


# データの準備
prefectures = ["愛知", "青森", "秋田", "石川", "茨城", "岩手", "愛媛", "大分", "大阪", "岡山", "沖縄", "香川", "鹿児島", "神奈川", "岐阜", "京都", "熊本", "群馬", "高知", "埼玉", "佐賀", "滋賀", "静岡", "島根", "千葉", "東京", "徳島", "栃木", "鳥取", "富山", "長崎", "長野", "奈良", "新潟", "兵庫", "広島", "福井", "福岡", "福島", "北海道", "三重", "宮城", "宮崎", "山形", "山口", "山梨", "和歌山"]
shipment = [568200, 31890, 31290, 42750, 307740, 56660, 49760, 41900, 432700, 108000, 5260, 48460, 44426, 368000, 190700, 110135, 66606, 186800, 20500, 579061, 95854, 136337, 245432, 22312, 299485, 590563, 29742, 175261, 37638, 79498, 34208, 136107, 136185, 83490, 291440, 176795, 54484, 181329, 110327, 42334, 159100, 177242, 37838, 39263, 65914, 99420, 35777]

# 棒グラフの描画
draw_bar_graph(prefectures, shipment)

# 出荷量が大きい順に並べ替えた棒グラフの描画
draw_sorted_bar_graph(prefectures, shipment)
