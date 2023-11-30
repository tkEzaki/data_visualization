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
shipment = [568212, 31895, 31295, 42741, 307752, 56667, 49767, 41907, 432778, 108003, 5240, 48454, 44466, 368026, 190720, 110115, 66604, 186811, 20554, 579061, 95824, 136137, 240432, 22612, 299455, 580563, 29745, 175267, 37678, 79298, 34208, 136407, 136385, 83590, 291430, 176715, 53484, 181309, 110027, 42324, 159106, 177842, 37888, 39663, 65910, 99220, 35777]

# 棒グラフの描画
draw_bar_graph(prefectures, shipment)

# 出荷量が大きい順に並べ替えた棒グラフの描画
draw_sorted_bar_graph(prefectures, shipment)
