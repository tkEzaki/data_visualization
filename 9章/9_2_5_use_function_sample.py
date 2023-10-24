import numpy as np
from scipy import stats


def generate_data():
    """データを生成する関数"""
    return np.array([170, 175, 160, 155, 180, 165, 171, 200, 152, 169,
                     166, 173, 168, 176, 158, 159, 161, 177, 140, 190])


def remove_outliers(data):
    """外れ値を除く関数"""
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return data[(data >= lower_bound) & (data <= upper_bound)]


def z_score(data):
    """zスコア化する関数"""
    return stats.zscore(data)


heights = generate_data()
heights_without_outliers = remove_outliers(heights)
heights_z_score = z_score(heights_without_outliers)

print(heights_z_score)