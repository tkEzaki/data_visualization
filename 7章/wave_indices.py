import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import pyhrv

# PhysioNetからデータをダウンロードして読み込む例
# wfdb.dl_database('mitdb', dl_dir='mitdb')  # データベース名とダウンロード先ディレクトリを指定

record = wfdb.rdrecord('mitdb/100', sampto=3000)
annotation = wfdb.rdann('mitdb/100', 'atr', sampto=3000)


# 2. ECGデータを可視化する
plt.figure(figsize=(8, 4))
# plt.plot(record.p_signal)
plt.plot(record.p_signal[:, 0])  # 最初のチャンネルだけをプロット
# plt.title("ECG Sample Data")
plt.xlabel("Time")
plt.ylabel("ECG Amplitude [mV]")

plt.tight_layout()
plt.savefig('ecg_sample.png', dpi=300)
plt.show()


record = wfdb.rdrecord('mitdb/100')  # , sampto=10000)
annotation = wfdb.rdann('mitdb/100', 'atr')  # , sampto=10000)

# 3. R-ピークを検出する
ecg_signal = record.p_signal[:, 0]
peaks, _ = find_peaks(ecg_signal, height=0.5)

# 4. 心拍変動（HRV）を計算する
rr_intervals = np.diff(peaks)

# LF/HF比を計算
results = pyhrv.frequency_domain.welch_psd(nni=rr_intervals)


print("LF/HF Ratio:", results)
