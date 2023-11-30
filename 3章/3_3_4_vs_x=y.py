import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする
import numpy as np  # 数値計算のためのNumPy
import pandas as pd  # データフレーム操作のためのPandas

plt.rcParams["font.size"] = 14  # プロットのフォントサイズを14に設定

num_users = 100  # ユーザー数

np.random.seed(0)  # 同じ乱数が生成されるようにシードを設定
replies_sent = np.zeros(num_users)  # 送信したリプライ数
replies_received = np.zeros(num_users)  # 受信したリプライ数

for i in range(num_users):
    pattern = np.random.choice(
        ['moderate', 'one_sided_few', 'one_sided_many'])  # 3つのパターンからランダムに選択
    if pattern == 'moderate':
        # お互いにそれなりの回数を送り合っている
        replies_sent[i] = np.random.randint(
            low=10, high=30)  # 10～30回の間でランダムに送信
        replies_received[i] = replies_sent[i] + \
            np.random.randint(low=-3, high=3)  # 送信した回数±3回の間でランダムに受信
        replies_sent[num_users - i - 1] = replies_received[i]  # 対称なユーザーの送信数を設定
        replies_received[num_users - i - 1] = replies_sent[i]  # 対称なユーザーの受信数を設定
    elif pattern == 'one_sided_few':
        # 片方が全く送らずにもう片方が０～３回送っている
        replies_sent[i] = np.random.randint(low=0, high=4)  # 0～3回の間でランダムに送信
        replies_received[i] = 0  # 受信は0回
        # やや非対称なユーザーの送信数を設定
        replies_sent[num_users - i - 1] = replies_received[i]
        replies_received[num_users - i -
                         1] = replies_sent[i]  # やや非対称なユーザーの受信数を設定
    else:  # pattern == 'one_sided_many'
        # 片方が全く送らずにもう片方が２０回くらい送っている
        replies_sent[i] = np.random.randint(
            low=10, high=30)  # 10～30回の間でランダムに送信
        replies_received[i] = 0  # 受信は0回
        # 非対称なユーザーの送信数を設定
        replies_sent[num_users - i - 1] = replies_received[i]
        replies_received[num_users - i -
                         1] = replies_sent[i]  # 非対称なユーザーの受信数を設定


# データフレームにまとめる
df = pd.DataFrame({
    'Sent': replies_sent,
    'Received': replies_received,
})


# 体重データを生成
weights_1 = np.random.normal(60, 2, 50)  # 平均60、分散10の正規分布
weights_2 = weights_1 + np.random.normal(-1, 0.5, 50)  # 平均-1、分散0.5の正規分布

# データフレームにまとめる
df_weights = pd.DataFrame({
    'Weight1': weights_1,
    'Weight2': weights_2,
})


# 図の描画
fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # 1行2列のグラフを作成


axs[0].scatter(df_weights['Weight1'], df_weights['Weight2'],
               color='orange', label='Weight Pair')  # 散布図の描画

# 範囲を揃えるためにx軸とy軸の最小・最大値を取得
lims = [
    np.min([axs[0].get_xlim(), axs[0].get_ylim()]),  # min of both axes
    np.max([axs[0].get_xlim(), axs[0].get_ylim()]),  # max of both axes
]
axs[0].plot(lims, lims, color='black', label='y=x')  # y=xの直線を描画
axs[0].set_xlim(lims)  # x軸の範囲を設定
axs[0].set_ylim(lims)  # y軸の範囲を設定
axs[0].set_ylabel('一か月後体重 [kg]', fontsize=18)  # y軸ラベル
axs[0].set_xlabel('実験開始時体重 [kg]', fontsize=18)  # x軸ラベル
axs[0].set_aspect('equal', 'box')  # アスペクト比を等しく設定
axs[0].grid(True)  # グリッドを表示


# 散布図の描画
axs[1].scatter(df['Sent'], df['Received'],
               color='lightblue', label='User Pair')

# 範囲を揃えるためにx軸とy軸の最小・最大値を取得
lims = [
    np.min([axs[1].get_xlim(), axs[1].get_ylim()]),  # 両方の軸の範囲で最小の値
    np.max([axs[1].get_xlim(), axs[1].get_ylim()]),  # 両方の軸の範囲で最大の値
]

axs[1].plot(lims, lims, color='black', label='y=x')  # y=xの直線を描画
axs[1].set_xlim(lims)  # x軸の範囲を設定
axs[1].set_ylim(lims)  # y軸の範囲を設定
axs[1].set_aspect('equal', 'box')  # アスペクト比を等しく設定
axs[1].set_ylabel('受信したリプライ数', fontsize=18)  # y軸ラベル
axs[1].set_xlabel('送信したリプライ数', fontsize=18)  # x軸ラベル
axs[1].grid(True)  # グリッドを表示


plt.tight_layout()  # レイアウトの設定
plt.savefig('3_3_4_vs_x=y.png', dpi=300)  # 画像を保存
plt.show()  # 画面に表示
