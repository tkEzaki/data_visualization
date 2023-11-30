import seaborn as sns  # グラフ作成のためのSeaborn
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import japanize_matplotlib  # Matplotlibで日本語を使用可能にする
from sklearn.model_selection import train_test_split  # データの分割
from sklearn.linear_model import LinearRegression  # 線形回帰
from sklearn.metrics import mean_squared_error  # RMSEの計算
import matplotlib.cm as cm  # カラーマップのためのMatplotlib

plt.rcParams["font.size"] = 14  # フォントサイズの設定

# データの準備
penguins = sns.load_dataset("penguins")  # データセットの読み込み
species_list = penguins['species'].unique()  # データを種類ごとに分割


# 図の描画
plt.figure(figsize=(6, 6))  # 図のサイズを指定

# 'tab10'カラーマップの取得
cmap = cm.get_cmap('tab10')

for idx, species in enumerate(species_list):
    # 種類ごとにデータをフィルタリング
    penguins_species = penguins[penguins['species'] == species].copy()

    # 欠損値の処理
    penguins_species.dropna(inplace=True)

    # 特徴量とターゲットを定義
    X = penguins_species[['bill_length_mm',
                          'bill_depth_mm', 'flipper_length_mm']]
    y = penguins_species['body_mass_g']

    # データの分割
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

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


plt.xlabel('実際の体重 [g]', fontsize=18)  # x軸ラベル
plt.ylabel('モデルによる予測 [g]', fontsize=18)  # y軸ラベル
plt.grid(True)  # グリッド線を表示
plt.tight_layout()  # レイアウトの設定
plt.savefig('3_3_3_prediction_scatter.png', dpi=300)  # 画像として保存
plt.show()  # グラフの表示
