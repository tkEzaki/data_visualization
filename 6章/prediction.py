# 必要なライブラリのインポート
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.cm as cm

plt.rcParams['font.family'] = 'Yu Gothic'
plt.rcParams['font.size'] = 14

# データの読み込み
penguins = sns.load_dataset("penguins")

# データを種類ごとに分割
species_list = penguins['species'].unique()

# 図の初期化
plt.figure(figsize=(10, 5))
# 'tab10'カラーマップの取得
cmap = cm.get_cmap('tab10')

# カウンタ（横軸の位置を管理するため）
counter = 0

for idx, species in enumerate(species_list):
    # 種類ごとにデータをフィルタリング
    penguins_species = penguins[penguins['species'] == species].copy()

    # 欠損値の処理
    penguins_species.dropna(inplace=True)

    # 特徴量とターゲットを定義
    X = penguins_species[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']]
    y = penguins_species['body_mass_g']

    # データの分割
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # モデルの作成と学習
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 予測
    predictions = model.predict(X_test)

    # RMSEを計算
    rmse = mean_squared_error(y_test, predictions, squared=False)
    print(f'Root Mean Squared Error for {species}: {rmse}')

    # 横軸の位置を計算
    x_positions = np.arange(counter, counter + len(y_test))

    # 真の値と予測値のプロット
    plt.scatter(x_positions, y_test, color=cmap(idx), alpha=1.0, label=f'True {species}')
    plt.scatter(x_positions, predictions, marker='o', color="k", alpha=1.0, label=f'Predicted {species}')

    # 縦線で誤差を可視化
    for x, y1, y2 in zip(x_positions, y_test, predictions):
        plt.plot([x, x], [y1, y2], color=cmap(idx), linestyle='--', linewidth=1)

    # カウンタを更新
    counter += len(y_test) + 2  # 種類ごとに間隔を開けるために+2

# グラフの設定
plt.xlabel('個体番号')
plt.ylabel('体重 [g]')
# plt.title('Scatter plot of True vs Predicted values for all species')
# plt.grid(True)
# plt.legend()
plt.tight_layout()
plt.savefig('modified_prediction.png', dpi=300)
plt.show()
