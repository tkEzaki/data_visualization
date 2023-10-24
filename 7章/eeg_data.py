import mne
import matplotlib.pyplot as plt
import pyhrv

# サンプルデータを読み込む
# MNEにはサンプルデータがいくつか含まれています
raw = mne.io.read_raw_fif(mne.datasets.sample.data_path() py -+ '/MEG/sample/sample_audvis_raw.fif', preload=True)

# 基本的な信号可視化
raw.plot(duration=5, n_channels=30)




plt.show()
