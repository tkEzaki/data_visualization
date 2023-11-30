import numpy as np  # 数値演算のためのNumPy
from scipy.stats import lognorm, norm  # 正規分布のためのSciPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

plt.rcParams['font.size'] = 14  # フォントサイズを14に設定

# 対数正規分布のパラメータ
lognorm_params = (0.954, 0, np.exp(0.65))

# サンプルを生成
np.random.seed(0)  # 乱数のシードを設定（再現性のため）
lognorm_samples = lognorm.rvs(*lognorm_params, size=10000)  # サンプルを生成
log_lognorm_samples = np.log(lognorm_samples)  # 対数変換

# データを正規分布でフィット
lognorm_mu, lognorm_std = norm.fit(log_lognorm_samples)  # 平均と標準偏差を推定

# ヒストグラムとフィット結果をプロット
fig, axs = plt.subplots(1, 2, figsize=(10, 4))  # サブプロットの作成

# 対数正規分布
axs[0].hist(lognorm_samples, bins=30, alpha=0.5, color='blue',
            edgecolor='black', density=True)  # ヒストグラムを描画
axs[0].set_xlabel('観測値 $X$')  # x軸ラベル
axs[0].set_ylabel('相対頻度')  # y軸ラベル

# 対数変換後の対数正規分布
axs[1].hist(log_lognorm_samples, bins=30, alpha=0.5, color='blue',
            edgecolor='black', density=True)  # ヒストグラムを描画
x = np.linspace(log_lognorm_samples.min(),
                log_lognorm_samples.max(), 1000)  # x軸の値
axs[1].plot(x, norm.pdf(x, lognorm_mu, lognorm_std), 'r--', lw=2)  # 正規分布を描画
axs[1].set_xlabel('log $X$')  # x軸ラベル


plt.tight_layout()  # レイアウトの設定
plt.subplots_adjust(wspace=0.3, hspace=0.4)  # サブプロット間の余白を設定
plt.savefig('3_1_3_3_log_transform.png', dpi=300)  # 画像として保存
plt.show()  # 図の表示
