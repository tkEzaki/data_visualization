import matplotlib.pyplot as plt  # matplotlibのpyplotをpltとしてインポート
import numpy as np               # numpyをnpとしてインポート
import pandas as pd              # pandasをpdとしてインポート
import japanize_matplotlib       # matplotlibで日本語を表示可能にする

plt.rcParams["font.size"] = 20   # プロットのフォントサイズを20に設定

# 与えられたデータ
data = {
    'x': [0.204, 1.07, -0.296, 0.57, 0.637, 0.82, 0.137, -0.046],
    'y': [0.07, 0.57, 0.936, 1.436, 0.32, 1.003, 1.186, 0.503]
}

df = pd.DataFrame(data)  # データフレームにデータを格納

# 四角形を形成する4点の座標を定義
square_points = np.array([
    [-0.296, 0.936],
    [0.57, 1.436],
    [1.07, 0.57],
    [0.204, 0.07],
    [-0.296, 0.936]
])

# 点をプロット
plt.scatter(df['x'], df['y'], label='Points', color='blue')

# 四角形を点で結んでプロット
plt.plot(square_points[:, 0], square_points[:, 1], 'r--', label='Square')

# ラベルとタイトルを追加
plt.xlabel('$x$')  # x軸ラベル
plt.ylabel('$y$')  # y軸ラベル

plt.axis('equal')  # x軸とy軸のスケールを等しく設定
plt.tight_layout() # レイアウトを整える
plt.savefig('1_2_2_square_scatter.png', dpi=300)  # png形式で保存
plt.show()  # プロットを表示
