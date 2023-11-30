import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ
from sklearn.mixture import GaussianMixture  # 混合ガウシアンモデル
from scipy.stats import norm  # 正規分布のためのSciPy

np.random.seed(0)  # 乱数のシードを設定（再現性のため）

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定

# ピーク一つとピーク二つの分布
data4_b = np.concatenate(
    [np.random.normal(3, 1, 500), np.random.normal(7, 1, 500)]
)  # 平均3、標準偏差1の正規分布と平均7、標準偏差1の正規分布に従う乱数を500個ずつ生成


plt.figure(figsize=(5, 4))  # グラフのサイズを指定

# データをヒストグラムでプロット
plt.hist(data4_b, bins=30, density=True, alpha=0.5,
         color='yellow', edgecolor='black')

# データを2成分のガウシアン混合モデルでフィッティング
gmm = GaussianMixture(n_components=2)  # 混合ガウシアンモデルのインスタンスを生成
gmm.fit(data4_b.reshape(-1, 1))  # 混合ガウシアンモデルのパラメータを推定

# 混合ガウシアンモデルの結果をプロット
x = np.linspace(data4_b.min(), data4_b.max(), 1000).reshape(-1, 1)  # x軸の値
logprob = gmm.score_samples(x)  # 対数尤度を計算（対数尤度として確率を計算する）
pdf = np.exp(logprob)  # 対数尤度を指数化
plt.plot(x, pdf, '-k', color='grey', alpha=0.5, lw=5)  # 密度関数を描画

# 各ガウシアンをプロット
colors = ['red', 'blue']  # 各ガウシアンの色
for i in range(gmm.n_components):
    pdf_individual = gmm.weights_[
        i] * norm(gmm.means_[i, 0], np.sqrt(gmm.covariances_[i, 0])).pdf(x)  # 各ガウシアンの密度関数
    plt.plot(x, pdf_individual, '--', color=colors[i])  # 各ガウシアンを描画

plt.xlabel('観測値 $X$')  # x軸ラベル
plt.tight_layout()  # レイアウトの設定
plt.savefig('3_1_3_2_gmm_fitting.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
