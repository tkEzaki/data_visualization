import pandas as pd

# CSVファイルからDataFrameを読み込む
df = pd.read_csv('data.csv')

# 辞書からDataFrameを作成
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'a', 'c']})

# DataFrameの最初の数行を表示（デフォルトは5行）
df.head()

# DataFrameの各列の統計的な情報（平均、標準偏差など）を表示
df.describe()

# DataFrameの特定の列を選択
df['A']

# DataFrameから特定の条件にマッチする行だけ取り出す
df_filtered = df[df['A'] > 1]

# 欠損値（NaN）を別の値で埋める
df.fillna(0)

# DataFrameをソート（ここでは列Aで昇順ソート）
df.sort_values(by='A')

# グループ化（ここでは列Aの値でグループ化して、それぞれのグループで列Bの値を合計）
df.groupby('B')['A'].sum()

# 新しい列を追加（ここでは列Aの値に1を加えた新しい列Cを作成）
df['C'] = df['A'] + 1

# DataFrameの行と列の名前を変更
df.rename(columns={'A': 'X', 'B': 'Y'}, inplace=True)

# DataFrameをCSVファイルとして保存（実際には保存先のファイルパスを指定）
df.to_csv('new_data.csv', index=False)
