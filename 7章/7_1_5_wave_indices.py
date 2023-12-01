import wfdb  # pip install wfdb でインストール
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
from scipy.signal import find_peaks  # R-ピーク検出のためのSciPy
import pyhrv  # pip install pyhrv でインストール
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams["font.size"] = 15

# PhysioNetからデータをダウンロードして読み込む例
wfdb.dl_database('mitdb', dl_dir='mitdb')  # データベース名とダウンロード先ディレクトリを指定
record = wfdb.rdrecord('mitdb/100', sampto=3000) 
annotation = wfdb.rdann('mitdb/100', 'atr', sampto=3000)


# ECGデータを可視化する
plt.figure(figsize=(8, 4))
plt.plot(record.p_signal[:, 0])  # 最初のチャンネルだけをプロット
plt.xlabel("Time")  # x軸ラベル
plt.ylabel("ECG Amplitude [mV]")  # y軸ラベル

plt.tight_layout()  # レイアウトの設定
plt.savefig('7_1_5_1_ecg_sample.png', dpi=300)  # PNG形式で保存
plt.show()  # 図の表示

# HRV 分析を実施する
plt.rcParams["font.size"] = 10  # フォントサイズを10に設定
record = wfdb.rdrecord('mitdb/100')  # , sampto=10000)
annotation = wfdb.rdann('mitdb/100', 'atr')  # , sampto=10000)

# R-ピークを検出する
ecg_signal = record.p_signal[:, 0]
peaks, _ = find_peaks(ecg_signal, height=0.5)

# 心拍変動（HRV）を計算する
rr_intervals = np.diff(peaks)

# LF/HF比を計算
results = pyhrv.frequency_domain.welch_psd(nni=rr_intervals, show=False)

plt.savefig('7_1_5_2_welch_psd_results.png', dpi=300)  # PNG形式で保存
plt.show()  # 図の表示
print("LF/HF Ratio:", results)
