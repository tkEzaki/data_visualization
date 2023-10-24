import seaborn as sns
import matplotlib.pyplot as plt
import japanize_matplotlib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.cm as cm

plt.rcParams["font.size"] = 14

# データの読み込み
penguins = sns.load_dataset("penguins")

# データを種類ごとに分割
species_list = penguins['species'].unique()

# 図の初期化
plt.figure(figsize=(6, 6))  # 図の大きさを正方形に変更

# 'tab10'カラーマップの取得
cmap = cm.get_cmap('tab10')

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

    # 真の値と予測結果の散布図をプロット
    plt.scatter(y_test, predictions, color=cmap(idx), alpha=1.0, label=species)

    # RMSEを計算
    rmse = mean_squared_error(y_test, predictions, squared=False)
    print(f'Root Mean Squared Error for {species}: {rmse}')

# x=y line
plt.plot([3000, 6000], [3000, 6000], color='black')

# 描画範囲を限定
# plt.xlim(2500, 6500)
# plt.ylim(2500, 6500)

plt.xlabel('実際の体重 [g]', fontsize=18)
plt.ylabel('モデルによる予測 [g]', fontsize=18)
# plt.title('Scatter plot of True vs Predicted values for all species')
plt.grid(True)
# plt.legend()
# plt.axis('equal')
plt.tight_layout()
plt.savefig('3_3_3_prediction_scatter.png', dpi=300)
plt.savefig('3_3_3_prediction_scatter.svg', dpi=300)

plt.show()
