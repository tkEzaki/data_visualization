import numpy as np  # 数値演算のためのNumPy
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import seaborn as sns  # グラフ作成のためのSeaborn
import japanize_matplotlib  # Matplotlibで日本語を表示するためのライブラリ

def set_plot_font_size(size=14):
    plt.rcParams['font.size'] = size

# サイコロの実験をシミュレーションする関数
def simulate_dice_experiment(n_trials):
    np.random.seed(0)  # シード値を固定
    
    # ボーナスタイムと通常時の確率
    bonus_prob = [1 / 11, 2 / 11, 2 / 11, 2 / 11, 2 / 11, 2 / 11]
    normal_prob = [2 / 11, 9 / 55, 9 / 55, 9 / 55, 9 / 55, 9 / 55]

    # 結果の格納用
    heatmap_data = np.zeros((6, 6))
    bonus_time_die1 = []
    bonus_time_die2 = []
    samples_die1 = []
    samples_die2 = []
    bonus_time = False

    for _ in range(n_trials):
        if bonus_time:
            die1 = np.random.choice(range(1, 7), p=bonus_prob)  # ボーナスタイム時のサイコロAの出目
            die2 = np.random.choice(range(1, 7), p=bonus_prob)  # ボーナスタイム時のサイコロBの出目
            # 結果を格納
            samples_die1.append(die1)
            samples_die2.append(die2)
            bonus_time_die1.append(die1)
            bonus_time_die2.append(die2)
        else:
            die1 = np.random.choice(range(1, 7), p=normal_prob)  # 通常時のサイコロAの出目
            die2 = np.random.choice(range(1, 7), p=normal_prob)  # 通常時のサイコロBの出目
            # 結果を格納
            samples_die1.append(die1)
            samples_die2.append(die2)

        heatmap_data[die1 - 1, die2 - 1] += 1
        bonus_time = (die1 == 1)

    heatmap_data = heatmap_data / np.sum(heatmap_data)

    return heatmap_data, samples_die1, samples_die2, bonus_time_die1, bonus_time_die2


# ヒートマップを描画する関数
def plot_heatmap(heatmap_data):
    plt.figure(figsize=(4.5, 4))
    sns.heatmap(heatmap_data, annot=True, fmt=".3f",
                annot_kws={'size': 10}, cmap='coolwarm',
                xticklabels=range(1, 7), yticklabels=range(1, 7),
                vmin=0.0139, vmax=0.031)
    plt.xlabel("サイコロBの出目")  # x軸ラベルを設定
    plt.ylabel("サイコロAの出目")  # y軸ラベルを設定
    plt.tight_layout()  # レイアウトの設定
    plt.savefig("6_4_3_1_dice_experiment_2_heatmap.png", dpi=300)  # 図の保存
    plt.show()  # 図の表示


# サイコロAが1が出たときのサイコロBの結果を棒グラフで描画する関数
def plot_bonus_time_bar(samples_die1, samples_die2):
    plt.figure(figsize=(4, 4))

    # np.arrayに変換
    samples_die1 = np.array(samples_die1)
    samples_die2 = np.array(samples_die2)

    # データの集計
    counts, _ = np.histogram(samples_die2[samples_die1 == 1], bins=range(1, 8))
    
    # 棒グラフの描画
    plt.bar(range(1, 7), counts / np.sum(counts), color='blue')
    plt.xticks(range(1, 7))  # x軸の目盛りを設定
    plt.xlabel("サイコロBの出目")  # x軸ラベルを設定
    plt.ylabel("相対頻度")  # y軸ラベルを設定
    plt.tight_layout()  # レイアウトの設定
    plt.savefig("6_4_3_2_dice_experiment_2_bar.png", dpi=300)  # 図の保存
    plt.show()  # 図の表示


# サンプルされた二つのサイコロの時系列を折れ線グラフで示す関数
def plot_time_series(samples_die1, samples_die2):
    plt.figure(figsize=(6, 3))
    plt.plot(range(1, 51), samples_die1[:50],
             label='Die 1', marker='o', linestyle='-')
    plt.plot(range(1, 51), samples_die2[:50],
             label='Die 2', marker='o', linestyle='-')
    
    # サイコロAで1が出た場合（ボーナスタイム）に背景色をつける
    for i, val in enumerate(samples_die1[:49], start=1):
        if val == 1:
            plt.axvspan(i + 0.5, i + 1.5, color='yellow', alpha=0.3)
    
    plt.xlabel("試行回数")  # x軸ラベルを設定
    plt.ylabel("サイコロの出目")  # y軸ラベルを設定
    plt.grid(True)  # グリッド線を表示
    plt.tight_layout()  # レイアウトの設定
    plt.savefig("6_4_4_1_dice_experiment_2_time_series.png", dpi=300)  # 図の保存
    plt.show()  # 図の表示


# ボーナスタイム時の棒グラフを描画する関数
def plot_conditioned_bar(bonus_time_die1, bonus_time_die2):
    plt.figure(figsize=(6, 3))
    plt.subplot(1, 2, 1)

    # データの集計
    counts1, _ = np.histogram(bonus_time_die1, bins=range(1, 8))
    
    # 棒グラフの描画
    plt.bar(range(1, 7), counts1 / np.sum(counts1), alpha=0.7,
            color='blue', edgecolor='black')
    plt.xticks(range(1, 7))  # x軸の目盛りを設定
    plt.xlabel("サイコロAの出目")  # x軸ラベルを設定
    plt.ylabel("相対頻度")  # y軸ラベルを設定
    
    plt.subplot(1, 2, 2)
    # データの集計
    counts2, _ = np.histogram(bonus_time_die2, bins=range(1, 8))

    # 棒グラフの描画
    plt.bar(range(1, 7), counts2 / np.sum(counts2),
            alpha=0.7, color='red', edgecolor='black')
    plt.xticks(range(1, 7))  # x軸の目盛りを設定
    plt.xlabel("サイコロBの出目")  # x軸ラベルを設定
    plt.ylabel("相対頻度")  # y軸ラベルを設定
    plt.tight_layout()  # レイアウトの設定
    plt.savefig("6_4_4_2_dice_experiment_2_conditioned_bar.png", dpi=300)  # 図の保存
    plt.show()  # 図の表示


if __name__ == '__main__':
    heatmap_data, samples_die1, samples_die2, bonus_time_die1, bonus_time_die2 = simulate_dice_experiment(100000)
    plot_heatmap(heatmap_data)
    plot_bonus_time_bar(samples_die1, samples_die2)
    plot_time_series(samples_die1, samples_die2)
    plot_conditioned_bar(bonus_time_die1, bonus_time_die2)