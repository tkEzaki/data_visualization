import numpy as np
from scipy import stats

# 適当に生成した20人分の身長のデータ（単位はcm）
heights = np.array([170, 175, 160, 155, 180, 165, 171, 200, 152, 169,
                    166, 173, 168, 176, 158, 159, 161, 177, 140, 190])

# 外れ値を除く
# ここでは、Q1 - 1.5 * IQR と Q3 + 1.5 * IQR を使用して外れ値を判定
Q1 = np.percentile(heights, 25)
Q3 = np.percentile(heights, 75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

heights_without_outliers = heights[
    (heights >= lower_bound) & (heights <= upper_bound)
]

# zスコア化
heights_z_score = stats.zscore(heights_without_outliers)

print(heights_z_score)
