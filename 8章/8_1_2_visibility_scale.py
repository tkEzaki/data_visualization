import matplotlib.pyplot as plt
import japanize_matplotlib

plt.rcParams["font.size"] = 14
# データの定義
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [11, 11.2, 11.5, 12, 12.2, 13, 14.2, 14.5, 15, 15.6, 16]
y2 = [11.1, 11.3, 11.4, 11.9, 12.1, 12.8, 14.0, 14.2, 14.7, 15.0, 15.5]

# グラフパターンと保存設定
patterns = [
    {'figsize': (5, 3), 'ylim': (10.5, 16.5), 'filename': '1_scale_example'},
    {'figsize': (5, 3), 'ylim': (0, 30), 'filename': '2_scale_example'},
    {'figsize': (9, 3), 'ylim': (10.5, 16.5), 'filename': '3_scale_example'},
    {'figsize': (3, 6), 'ylim': (10.5, 16.5), 'filename': '4_scale_example'},
]

for pattern in patterns:
    plt.figure(figsize=pattern['figsize'])

    plt.plot(x, y1, label='y1', marker='o')
    plt.plot(x, y2, label='y2', marker='x')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(pattern['ylim'])

    plt.legend()
    plt.tight_layout()

    # PNGとSVGで保存
    plt.savefig(f"8_1_2_{pattern['filename']}.png")
    plt.savefig(f"8_1_2_{pattern['filename']}.svg")

    # グラフの表示（オプション）
    # plt.show()

    # グラフをクリア
    plt.clf()
