from scipy import stats

# 正規分布に従う乱数を生成
normal_data = stats.norm.rvs(loc=0, scale=1, size=100)

# 正規分布の確率密度関数（PDF）を計算
norm_pdf = stats.norm.pdf(0, loc=0, scale=1)

# データの基本的な記述統計量を計算
mean, variance, skewness, kurtosis = stats.describe(normal_data)

# ヒストグラムから確率密度関数を推定
hist_density = stats.relfreq(normal_data, numbins=10)

# ピアソンの相関係数を計算
pearson_corr, _ = stats.pearsonr([1, 2, 3], [1, 2, 3])

# データをzスコアに変換
z_scores = stats.zscore([1, 2, 3, 4, 5])

# t検定を行う（2つの独立したサンプル）
t_stat, p_val = stats.ttest_ind([1, 2, 3], [1.1, 2.1, 3.1])

# 単純な線形回帰（最小二乗法）
slope, intercept, r_val, p_val_reg, std_err = stats.linregress([1, 2, 3], [1, 4, 9])


