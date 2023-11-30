import numpy as np
from hmmlearn import hmm  # 隠れマルコフモデルのためのライブラリ pip install hmmlearnでインストール
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
from matplotlib.colors import ListedColormap, Normalize  # カラーマップのためのMatplotlib
from matplotlib.gridspec import GridSpec  # グラフ描画のためのMatplotlib
from matplotlib.colorbar import Colorbar  # カラーバーのためのMatplotlib
import seaborn as sns  # グラフ作成のためのSeaborn
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする


plt.rcParams['font.size'] = 14  # プロットのフォントサイズを14に設定

# 半正定値行列の生成


def generate_positive_semi_definite(n):
    M = np.random.randn(n, n)
    return np.dot(M, M.transpose())


# パラメータ設定
n_samples = 101  # 時系列の長さ
n_features = 5  # 多次元の次元数
n_components = 3  # 隠れ状態の数

# 隠れマルコフモデル（HMM）の初期化
model = hmm.GaussianHMM(n_components=n_components, covariance_type="full")

# モデルのパラメータをランダムに初期化
np.random.seed(2)
model.startprob_ = np.random.random(n_components)
model.startprob_ /= model.startprob_.sum()
model.transmat_ = np.random.random((n_components, n_components))
model.transmat_ /= model.transmat_.sum(axis=1, keepdims=True)
model.means_ = np.random.random((n_components, n_features))
model.covars_ = np.stack(
    [generate_positive_semi_definite(n_features) for _ in range(n_components)]
)

# HMMからデータを生成
X, Z = model.sample(n_samples)

# 隠れ状態の推定
Z_pred = model.predict(X)
# Z_pred の解像度を100倍にする
Z_pred_100 = np.repeat(Z_pred, 100)

# 描画設定
fig = plt.figure(figsize=(10, 10))  # サブプロットの作成
gs = GridSpec(8, 4, height_ratios=[1] * 5 +
              [0.8] + [2.5, 0.5], hspace=0.5)  # レイアウトのためにGridSpecを使用

cmap = plt.get_cmap('jet')  # カラーマップを設定
norm = Normalize(vmin=-3, vmax=3)  # カラーマップの範囲を設定
cmap_state = ListedColormap(
    cmap(norm(np.arange(n_components))))  # 隠れ状態のカラーマップを設定
cmap_tr = plt.get_cmap('coolwarm')  # カラーマップを設定
norm_tr = Normalize(vmin=0, vmax=1)  # カラーマップの範囲を設定
norm_mean = Normalize(vmin=0, vmax=1)  # カラーマップの範囲を設定

# 時系列の描画
for i in range(n_features):
    ax = plt.subplot(gs[i, 0:4])  # サブプロットを作成
    ax.set_ylim(-10, 10)  # y軸の範囲を設定
    ax.set_xlim(0, n_samples - 1)  # x軸の範囲を設定
    ax.plot(X[:, i])  # 時系列をプロット
    for state in range(n_components):
        ax.fill_between(
            np.arange(0, n_samples, 0.01), -10, 10,
            where=(Z_pred_100 == state),
            color=cmap_state(state), alpha=0.3
        )  # 隠れ状態の領域を塗りつぶし

    ax.set_ylabel(f'変数 {i+1}')  # y軸ラベルを設定
    if i == n_features - 1:
        ax.set_xlabel('時間ステップ')  # x軸ラベルを設定

# 各共分散行列の描画
state_names = ['A', 'B', 'C']
for i in range(n_components):
    ax = plt.subplot(gs[n_features + 1:n_features + 2, i])
    sns.heatmap(
        model.covars_[i], ax=ax, cmap=cmap,
        norm=norm, cbar=True, cbar_kws={"ticks": [-3, 0, 3]}
    )  # 共分散行列を描画

    ax.set_title(f'状態 {state_names[i]}')  # タイトルを設定
    if i == 0:
        ax.set_ylabel('共分散行列\n')  # y軸ラベルを設定

    ax.set_xticks(np.arange(n_features) + 0.5)  # x軸の目盛りを設定
    ax.set_yticks(np.arange(n_features) + 0.5)  # y軸の目盛りを設定
    ax.set_xticklabels(np.arange(1, n_features + 1))  # x軸の目盛りラベルを設定
    ax.set_yticklabels(np.arange(1, n_features + 1),
                       rotation=0)  # y軸の目盛りラベルを設定
    # 軸線の表示
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)


# 遷移行列の描画
axs_t = plt.subplot(gs[n_features + 1:n_features + 2, 3])

sns.heatmap(model.transmat_, ax=axs_t, cmap=cmap_tr,
            norm=norm_tr, cbar=True)  # 遷移行列を描画
axs_t.set_title('状態遷移行列')  # タイトルを設定
axs_t.set_xticklabels(['A', 'B', 'C'])  # x軸の目盛りラベルを設定
axs_t.set_yticklabels(['A', 'B', 'C'], rotation=0)  # y軸の目盛りラベルを設定
# 軸線の表示
axs_t.spines['top'].set_visible(True)
axs_t.spines['right'].set_visible(True)
axs_t.spines['bottom'].set_visible(True)
axs_t.spines['left'].set_visible(True)


# 各平均の描画
for i in range(n_components):
    ax = plt.subplot(gs[n_features + 2, i])

    sns.heatmap(
        model.means_[i].reshape(1, -1), ax=ax, cmap=cmap,
        norm=norm_mean, cbar=True, cbar_kws={"aspect": 4}
    )  # 平均を描画

    if i == 0:
        ax.set_ylabel('平均\n\n')  # y軸ラベルを設定
        ax.set_yticks([])  # y軸の目盛りを非表示
    else:
        ax.yaxis.set_visible(False)  # y軸を非表示

    if i == 1:
        ax.set_xlabel('変数')  # x軸ラベルを設定

    ax.set_xticks(np.arange(n_features) + 0.5)  # x軸の目盛りを設定
    ax.set_xticklabels(np.arange(1, n_features + 1))  # x軸の目盛りラベルを設定
    # 軸線の表示
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)

plt.savefig('4_3_7_hmm.png', dpi=300)  # 画像を保存
plt.show()  # 画像を画面に表示
