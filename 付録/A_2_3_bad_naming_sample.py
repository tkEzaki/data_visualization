import numpy as np
from scipy import stats

# データ
a = np.array([170, 175, 160, 155, 180, 165, 171, 200, 152, 169,
              166, 173, 168, 176, 158, 159, 161, 177, 140, 190])

# 外れ値処理
b = np.percentile(a, 25)
c = np.percentile(a, 75)
d = c - b

e = b - 1.5 * d
f = c + 1.5 * d

g = a[(a >= e) & (a <= f)]

# zスコア化
h = stats.zscore(g)

print(h)
