import matplotlib.pyplot as plt

fig, ax = plt.subplots()  # グラフを描画する領域を作成


# 軸周辺の設定（axに対して）
ax.set_xlabel('X-axis')  # X軸のラベルを設定
ax.set_ylabel('Y-axis')  # Y軸のラベルを設定
ax.set_title('Graph Title')  # グラフのタイトルを設定
ax.set_xticks([0, 1, 2])  # X軸の目盛りを設定
ax.set_xticklabels(['Zero', 'One', 'Two'])  # X軸の目盛りラベルを設定
ax.set_yticks([0, 1, 2])  # Y軸の目盛りを設定
ax.set_yticklabels(['Zero', 'One', 'Two'])  # Y軸の目盛りラベルを設定
ax.set_xlim(0, 10)  # X軸の範囲を設定
ax.set_ylim(0, 10)  # Y軸の範囲を設定
ax.set_xscale('log')  # X軸を対数スケールに設定
ax.set_yscale('log')  # Y軸を対数スケールに設定

# 軸周辺の設定（pltに対して）
plt.xlabel('X-axis')  # X軸のラベルを設定
plt.ylabel('Y-axis')  # Y軸のラベルを設定
plt.title('Graph Title')  # グラフのタイトルを設定
plt.xticks([0, 1, 2], ['Zero', 'One', 'Two'])  # X軸の目盛りを設定
plt.yticks([0, 1, 2], ['Zero', 'One', 'Two'])  # Y軸の目盛りを設定
plt.xlim(0, 10)  # X軸の範囲を設定（この例では0から10に）
plt.ylim(0, 10)  # Y軸の範囲を設定（この例では0から10に）
plt.xscale('log')  # X軸を対数スケールに設定
plt.yscale('log')  # Y軸を対数スケールに設定


# テキストや注釈の追加
plt.text(5, 5, 'This is text')  # 任意の位置にテキストを追加
plt.annotate(
    'This is an annotation',
    xy=(2, 2),
    xytext=(4, 4),
    arrowprops=dict(arrowstyle='->')
)  # 矢印付きの注釈を追加


# その他
plt.grid(True)  # グリッド線を追加
plt.legend(['Line1', 'Line2'])  # 凡例を追加
plt.savefig('graph.png')  # グラフをファイルに保存（他の形式も利用可能）
plt.show()  # グラフを表示
