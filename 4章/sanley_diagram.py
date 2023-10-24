import plotly.graph_objects as go
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# seabornライブラリからテストデータをロード
data = sns.load_dataset("titanic").dropna()

# カテゴリ変数をエンコード
label_encoder = LabelEncoder()
data['sex'] = label_encoder.fit_transform(data['sex'])
data['embarked'] = label_encoder.fit_transform(data['embarked'])

# サンキーグラフのソースとターゲットを定義
source = data['sex'].values
target = data['embarked'].values

# 各リンクの値を定義（ここではすべて1とする）
value = [1]*len(source)

# グラフの作成
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["Male", "Female", "Southampton", "Cherbourg", "Queenstown"],
      color = "blue"
    ),
    link = dict(
      source = source,
      target = target,
      value = value
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()
