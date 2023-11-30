import numpy as np  # numpyをnpとしてインポート
import matplotlib.pyplot as plt  # matplotlib.pyplotをpltとしてインポート
from scipy import stats  # scipyからstatsをインポート
import japanize_matplotlib  # matplotlibで日本語を使用するためのライブラリをインポート

# ヒートマップを生成する関数
def generate_heatmap():
    mean = [0, 0]  # 平均
    cov = [[1, 0.8], [0.8, 1]]  # 共分散行列
    x = np.random.multivariate_normal(mean, cov, (10, 10))  # 2変量正規分布からデータ生成
    heatmap1, heatmap2 = x[..., 0], x[..., 1]  # ヒートマップ用のデータ分割
    heatmap1 = (heatmap1 - np.min(heatmap1)) / (np.max(heatmap1) - np.min(heatmap1))  # 正規化
    heatmap2 = (heatmap2 - np.min(heatmap2)) / (np.max(heatmap2) - np.min(heatmap2))  # 正規化
    x = heatmap1.flatten()  # 1次元配列に変換
    y = heatmap2.flatten()  # 1次元配列に変換
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)  # 線形回帰分析

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # サブプロットの作成
    axs[0].imshow(heatmap1, cmap='gray', interpolation='nearest')  # ヒートマップ1の描画
    axs[0].axis('off')  # 軸の非表示
    axs[1].imshow(heatmap2, cmap='gray', interpolation='nearest')  # ヒートマップ2の描画
    axs[1].axis('off')  # 軸の非表示
    plt.savefig('1_1_6_visual_data.png')  # 画像として保存
    plt.show()

    plt.figure(figsize=(4, 4))  # 新しい図の作成
    plt.scatter(x, y, alpha=0.5)  # 散布図の描画
    plt.plot(x, intercept + slope * x, 'b')  # 回帰直線の描画
    plt.gca().set_aspect('equal', adjustable='box')  # アスペクト比の調整
    plt.xticks([0.0, 0.5, 1.0])  # x軸の目盛り設定
    plt.yticks([0.0, 0.5, 1.0])  # y軸の目盛り設定
    plt.tick_params(axis='both', which='major', labelsize=22)  # 目盛りの設定
    plt.tight_layout()  # レイアウトの調整
    plt.savefig('1_1_6_scatter.png', dpi=300)  # 画像として保存
    plt.show()
    print(f'Correlation coefficient: {r_value}, {p_value}')  # 相関係数とp値の出力

# 個体の位置データに関する関数
def generate_individual_location():
    individual1 = np.abs(np.random.normal(loc=0, scale=1, size=100))  # 個体1のデータ生成
    individual2 = np.abs(np.random.normal(loc=0, scale=1, size=100))  # 個体2のデータ生成
    individual2 = 0.6 * individual1 + 0.4 * individual2  # 個体2のデータ変換
    individual1 = individual1 / np.sum(individual1)  # 正規化
    individual2 = individual2 / np.sum(individual2)  # 正規化
    slope, intercept, r_value, p_value, std_err = stats.linregress(individual1, individual2)  # 線形回帰分析

    plt.figure(figsize=(6, 3))  # 新しい図の作成
    barWidth = 0.3  # バーの幅
    r1 = np.arange(len(individual1))  # 個体1のバーの位置
    r2 = [x + barWidth for x in r1]  # 個体2のバーの位置
    plt.bar(r1, individual1, color='b', width=barWidth, edgecolor='b')  # 個体1のバーチャート
    plt.bar(r2, individual2, color='r', width=barWidth, edgecolor='r')  # 個体2のバーチャート
    plt.xlim([0, 100])  # x軸の範囲設定
    plt.tick_params(axis='both', which='major', labelsize=18)  # 目盛りの設定
    plt.savefig('1_1_6_location_index.png', dpi=300)  # 画像として保存
    plt.show()

    plt.figure(figsize=(4, 4))  # 新しい図の作成
    plt.scatter(individual1, individual2, alpha=0.5, c="g")  # 散布図の描画
    plt.plot(individual1, intercept + slope * individual1, 'g')  # 回帰直線の描画
    plt.xlim([0, 0.03])  # x軸の範囲設定
    plt.ylim([0, 0.03])  # y軸の範囲設定
    plt.gca().set_aspect('equal', adjustable='box')  # アスペクト比の調整
    plt.xticks([0.0, 0.01, 0.02, 0.03])  # x軸の目盛り設定
    plt.yticks([0.0, 0.01, 0.02, 0.03])  # y軸の目盛り設定
    plt.tick_params(axis='both', which='major', labelsize=20)  # 目盛りの設定
    plt.tight_layout()  # レイアウトの調整
    plt.savefig('1_1_6_location_index_scatter.png', dpi=300)  # 画像として保存
    plt.show()
    print(f'Correlation coefficient: {r_value}, {p_value}')  # 相関係数とp値の出力

# メイン関数
if __name__ == "__main__":
    generate_heatmap()  # ヒートマップの生成
    generate_individual_location()  # 個体の位置データの生成
