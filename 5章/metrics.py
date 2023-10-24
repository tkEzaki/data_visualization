import matplotlib.pyplot as plt


plt.figure(figsize=(10, 3))

# 標準偏差の数式
plt.text(0.1, 0.5, r'$\mathrm{{標準偏差}} = \sqrt{{\frac{{1}}{{N}} \sum (X_i - \mu)^2}}$', fontsize=12)

# 平均絶対偏差の数式
plt.text(0.1, 0.3, r'$\mathrm{{平均絶対偏差}} = \frac{{1}}{{N}} \sum |X_i - \mu|$', fontsize=12)

# 中央絶対偏差の数式
plt.text(0.1, 0.1, r'$\mathrm{{中央絶対偏差}} = \mathrm{{median}}(|X_i - \mathrm{{median}}(X)|)$', fontsize=12)

plt.axis('off')  # 軸を非表示にする
plt.show()
