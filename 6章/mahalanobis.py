import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import mahalanobis
from numpy.linalg import inv
plt.rcParams['font.family'] = 'Yu Gothic'

# CSVファイルを読み込む
df = pd.read_csv('baseball_players.csv')
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
df['Mahalanobis'] = df.apply(lambda row: mahalanobis(row[['Height(m)', 'Weight(kg)']], mean_vector, inv_cov_matrix), axis=1)

# プロット（マハラビノス距離一定の複数の楕円を含む）
fig, ax = plt.subplots()
scatter = ax.scatter(df['Height(m)'], df['Weight(kg)'], c=df['Mahalanobis'], cmap='viridis')
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('マハラビノス距離')

max_mahalanobis = df['Mahalanobis'].max()
# マハラビノス距離が一定の楕円を複数描画（ここでは距離 1.0, 2.0, 3.0, 4.0 に対して）
for md in [1, 2, 3, 4]:
    ellipse_radius = md ** 2
    v, w = np.linalg.eigh(cov_matrix.iloc[:2, :2])
    v = 2.0 * np.sqrt(ellipse_radius) * np.sqrt(v)
    u = w[0] / np.linalg.norm(w[0])
    angle = np.arctan(u[1] / u[0])
    angle = 180.0 * angle / np.pi  # convert to degrees
    ellipse = plt.matplotlib.patches.Ellipse(mean_vector.iloc[:2], v[0], v[1], 180.0 + angle, linestyle="--", edgecolor='r', facecolor='none')
    ax.add_patch(ellipse)

plt.xlabel('身長 [m]')
plt.ylabel('体重 [kg]')
plt.savefig('mahalanobis.png', dpi=300)
plt.show()
