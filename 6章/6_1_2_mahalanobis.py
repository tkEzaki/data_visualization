import pandas as pd  # データフレーム作成のためのPandas
import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from scipy.spatial.distance import mahalanobis  # マハラノビス距離の計算のためのSciPy
from numpy.linalg import inv  # 逆行列の計算のためのNumPy
import japanize_matplotlib  # 日本語化のためのライブラリ
import matplotlib
print(matplotlib.__version__)

plt.rcParams['font.size'] = 15  # フォントサイズを設定

# CSVファイルを読み込む
df = pd.read_csv('baseball_players_dummy.csv')
# 再配布を避けるためGitHub上にはダミーデータを入れてありますが、元のデータは下記からDLできます。
# https://www.kaggle.com/datasets/ayessa/predict-baseball-players-position
# http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights


# 単位をSI単位に変換（Heightをメートルに、Weightをキログラムに）
df['Height(m)'] = df['Height(inches)'] * 0.0254
df['Weight(kg)'] = df['Weight(pounds)'] * 0.453592

# 共分散行列と平均ベクトルを計算
cov_matrix = df[['Height(m)', 'Weight(kg)']].cov()
inv_cov_matrix = inv(cov_matrix)
mean_vector = df[['Height(m)', 'Weight(kg)']].mean()

# マハラビノス距離を計算
df['Mahalanobis'] = df.apply(lambda row: mahalanobis(
    row[['Height(m)', 'Weight(kg)']], mean_vector, inv_cov_matrix), axis=1)

# プロット（マハラビノス距離一定の複数の楕円を含む）
fig, ax = plt.subplots()
scatter = ax.scatter(df['Height(m)'], df['Weight(kg)'],
                     c=df['Mahalanobis'], cmap='viridis')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('マハラビノス距離')

max_mahalanobis = df['Mahalanobis'].max()
# マハラビノス距離が一定の楕円を複数描画（ここでは距離 1.0, 2.0, 3.0, 4.0 に対して）
for md in [1, 2, 3, 4]:
    ellipse_radius = md ** 2  # 楕円の半径
    v, w = np.linalg.eigh(cov_matrix.iloc[:2, :2])  # 固有値と固有ベクトルを計算
    v = 2.0 * np.sqrt(ellipse_radius) * np.sqrt(v)  # 固有値を楕円の半径に変換
    u = w[0] / np.linalg.norm(w[0])  # 固有ベクトルの単位ベクトル
    angle = np.arctan(u[1] / u[0])  # 固有ベクトルの傾き（ラジアン）
    angle = 180.0 * angle / np.pi  # ラジアンを度に変換

    # 楕円を描画
    ellipse = plt.matplotlib.patches.Ellipse(
        mean_vector.iloc[:2], v[0], v[1], angle=180.0 + angle,
        linestyle="--", edgecolor='r', facecolor='none'
    )  # matlabのversionが少し古くてエラーになる場合は以下のように書くと動くかもしれません。
    # ellipse = plt.matplotlib.patches.Ellipse(mean_vector.iloc[:2], v[0], v[1], 180.0 + angle, linestyle="--", edgecolor='r', facecolor='none')

    ax.add_patch(ellipse)  # 楕円を描画

plt.xlabel('身長 [m]')  # x軸ラベル
plt.ylabel('体重 [kg]')  # y軸ラベル
plt.savefig('6_1_2_mahalanobis.png', dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
