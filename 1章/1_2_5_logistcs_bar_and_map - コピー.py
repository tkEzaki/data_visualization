import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import japanize_matplotlib
import numpy as np
import pandas as pd
from japanmap import picture

plt.rcParams["font.size"] = 14


def draw_bar_graph(prefectures, shipment):
    plt.figure(figsize=(12, 4))
    plt.bar(prefectures, shipment, width=0.5)
    plt.xticks(rotation=90)
    plt.xlim(-0.5, 46.5)
    plt.tight_layout()
    plt.savefig("1_2_5_logistics_bar.png")
    plt.show()


def draw_ordered_by_code_bar_graph(prefectures_ordered_by_code, ordered_shipments_by_code):
    plt.figure(figsize=(12, 4))
    plt.bar(prefectures_ordered_by_code, ordered_shipments_by_code, width=0.5)
    plt.xticks(rotation=90)
    plt.xlim(-0.5, 46.5)
    plt.tight_layout()
    plt.savefig("1_2_5_logistics_bar_ordered_by_code.png")
    plt.show()


def draw_japan_map(prefectures, shipment):
    shipment_log = np.log(shipment)
    df = pd.DataFrame({
        'prefecture': prefectures,
        'shipment_log': shipment_log
    })

    cmap = plt.get_cmap('jet')
    vmin = np.log(1000)
    vmax = np.log(1000000)

    plt.figure(figsize=(8, 6))
    norm = plt.Normalize(vmin=vmin, vmax=vmax)

    colors = [cmap(norm(value)) for value in df['shipment_log']]
    hex_colors = ['#' + bytes((int(r * 255), int(g * 255), int(b * 255))).hex() for r, g, b, _ in colors]
    img = picture(pd.Series(hex_colors, index=df['prefecture']))
    plt.imshow(img)
    plt.axis('off')

    mappable = plt.cm.ScalarMappable(norm, cmap)
    mappable.set_array([])
    cbar = plt.colorbar(mappable)
    ticks = np.log([1000, 10000, 100000, 1000000])
    cbar.set_ticks(ticks)
    cbar.set_ticklabels([1000, 10000, 100000, 1000000])
    
    plt.tight_layout()
    plt.savefig("1_2_5_logistics_map.svg", dpi=300)
    plt.show()


# データの準備
prefectures = ["愛知", "青森", "秋田", "石川", "茨城", "岩手", "愛媛", "大分", "大阪", "岡山", "沖縄", "香川", "鹿児島", "神奈川", "岐阜", "京都", "熊本", "群馬", "高知", "埼玉", "佐賀", "滋賀", "静岡", "島根", "千葉", "東京", "徳島", "栃木", "鳥取", "富山", "長崎", "長野", "奈良", "新潟", "兵庫", "広島", "福井", "福岡", "福島", "北海道", "三重", "宮城", "宮崎", "山形", "山口", "山梨", "和歌山"]
shipment = [568212, 31895, 31295, 42741, 307752, 56667, 49767, 41907, 432778, 108003, 5240, 48454, 44466, 368026, 190720, 110115, 66604, 186811, 20554, 579061, 95824, 136137, 240432, 22612, 299455, 580563, 29745, 175267, 37678, 79298, 34208, 136407, 136385, 83590, 291430, 176715, 53484, 181309, 110027, 42324, 159106, 177842, 37888, 39663, 65910, 99220, 35777]

# 棒グラフの描画
draw_bar_graph(prefectures, shipment)

# 都道府県コード順の出荷量棒グラフの描画
prefectures_ordered_by_code = ["北海道", "青森", "岩手", "宮城", "秋田", "山形", "福島", "茨城", "栃木", "群馬", "埼玉", "千葉", "東京", "神奈川", "新潟", "富山", "石川", "福井", "山梨", "長野", "岐阜", "静岡", "愛知", "三重", "滋賀", "京都", "大阪", "兵庫", "奈良", "和歌山", "鳥取", "島根", "岡山", "広島", "山口", "徳島", "香川", "愛媛", "高知", "福岡", "佐賀", "長崎", "熊本", "大分", "宮崎", "鹿児島", "沖縄"]
ordered_shipments_by_code = [42324, 31895, 56667, 177842, 31295, 39663, 110027, 307752, 175267, 186811, 579061, 299455, 580563, 368026, 83590, 79298, 42741, 53484, 99220, 136407, 190720, 240432, 568212, 159106, 136137, 110115, 432778, 291430, 136385, 35777, 37678, 22612, 108003, 176715, 65910, 29745, 48454, 49767, 20554, 181309, 95824, 34208, 66604, 41907, 37888, 44466, 5240]

draw_ordered_by_code_bar_graph(prefectures_ordered_by_code, ordered_shipments_by_code)

# 日本地図の描画
draw_japan_map(prefectures, shipment)
