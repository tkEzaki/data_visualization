import torchaudio  # pip install torchaudio でインストール
import matplotlib.pyplot as plt  # グラフ描画のためのMatplotlib
import numpy as np  # 数値演算のためのNumPy
from scipy.fftpack import fft, fftfreq, ifft  # FFTのためのSciPy
from scipy.signal import stft, cwt, morlet, ricker  # STFTと連続ウェーブレット変換のためのSciPy
import japanize_matplotlib  # 日本語化のためのライブラリ

plt.rcParams['font.size'] = 16  # フォントサイズを設定

# fftを計算する関数
def fourier_approximation(fft_values, n_terms, N, t):
    fft_approx = np.zeros_like(fft_values)
    # Keep only the first few terms
    fft_approx[:n_terms + 1] = fft_values[:n_terms + 1]
    fft_approx[-n_terms:] = fft_values[-n_terms:]
    # Compute the inverse FFT to get the time domain signal
    signal_approx = ifft(fft_approx).real
    return signal_approx

# torchaudioのバックエンドをsoundfileに設定
# pip install soundfile でインストール
torchaudio.set_audio_backend("soundfile")

# YESNOデータセットをダウンロードして読み込む　音声ファイルがダウンロードされるので注意
dataset = torchaudio.datasets.YESNO('.', download=True)
waveform_yesno, sample_rate, *_ = dataset[0]  # 最初のサンプルを取得
waveform_yesno = waveform_yesno.numpy().flatten()  # 1次元のNumPy配列に変換
t_yesno = np.linspace(0, len(waveform_yesno) / sample_rate, len(waveform_yesno), endpoint=False)  # 時間軸を計算


# 人工データを生成
sampling_rate = 44100工
duration = 1.0
N = int(sampling_rate * duration)
t = np.linspace(0, duration, N, endpoint=False)

# sine波の合成
freqs_sine = [2, 10, 20]
amplitudes_sine = [1, 0.5, 0.2]
sine_wave = np.sum([amplitudes_sine[i] * np.sin(2 * np.pi * freqs_sine[i] * t) for i in range(len(freqs_sine))], axis=0)

# 矩形波の合成
freq_square = 2
triangle_wave = 0.5 * (1 + np.sign(np.sin(2 * np.pi * freq_square * t)))


# プロット用にデータをまとめる
data_list = [sine_wave, triangle_wave, waveform_yesno]
titles = ['Three Sine Waves', 'Square Wave', 'YESNO Sample']
time_arrays = [t, t, t_yesno]

# サブプロットを作成
fig, axes = plt.subplots(len(data_list), 2, figsize=(10, 12))

for i, (data, title, time_array) in enumerate(zip(data_list, titles, time_arrays)):
    # 元の時系列プロット
    axes[i, 0].plot(time_array, data, label='Original', color="k", alpha=0.6)

    # フーリエ変換
    if title == 'Three Sine Waves':
        for n in [2, 10]:
            approx = fourier_approximation(fft(data), n, N, t)
            axes[i, 0].plot(time_array, approx, label=f'{n}-term Fourier Approx', linestyle='--', alpha=0.6)
    elif title == 'Squar Wave':
        for n in [5, 10, 50]:
            approx = fourier_approximation(fft(data), n, N, t)
            axes[i, 0].plot(time_array, approx, label=f'{n}-term Fourier Approx', linestyle='--', alpha=0.6)

    axes[i, 0].set_xlabel('時間 [s]')  # x軸のラベルを設定
    axes[i, 0].set_ylabel('')  # y軸のラベルを設定

    # 周波数領域プロット
    N_fft = len(data)
    freq_values = fftfreq(N_fft, 1 / sampling_rate)
    fft_values = fft(data)
    magnitude = np.abs(fft_values) / N  # Normalize
    
    # 正の周波数のみをプロット
    positive_freq_idxs = np.where(freq_values > 0)
    axes[i, 1].plot(freq_values[positive_freq_idxs], magnitude[positive_freq_idxs], color="k", alpha=0.6)
    axes[i, 1].set_xlabel('周波数 [Hz]')
    axes[i, 1].set_ylabel('振幅')

    # x軸範囲の設定
    if title == 'YESNO Sample':
        axes[i, 1].set_xlim([0, 5000])  # YESNO Sampleのみx軸範囲は広めにとる
    else:
        axes[i, 1].set_xlim([0, 50])


plt.tight_layout()  # レイアウトの設定
plt.savefig('7_1_3_fourier_analysis.png', dpi=300)  # 図の保存
plt.show()  # 図の表示


## STFTと連続ウェーブレット変換を図示する

plt.rcParams['font.size'] = 12  # フォントサイズを設定

fig, axes = plt.subplots(3, 1, figsize=(8, 6))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9, wspace=0.0, hspace=1.5) # 図の余白を設定

# YESNO sampleの時系列プロット
axes[0].plot(t_yesno, waveform_yesno, label='Original', color="k", alpha=0.6)
axes[0].set_xlabel('時間 [s]')
axes[0].set_ylabel('')
axes[0].set_xlim([0, 6])

# Short-Time Fourier Transform (STFT) を実施して可視化
frequencies, time_stft, Zxx = stft(waveform_yesno, fs=sample_rate, nperseg=128)
pcm = axes[1].pcolormesh(time_stft, frequencies, np.abs(Zxx), shading='gouraud', cmap='jet')  # STFTの結果をプロット
axes[1].set_xlabel('時間 [s]')  # x軸のラベルを設定
axes[1].set_ylabel('周波数 [Hz]')  # y軸のラベルを設定
axes[1].set_xlim([0, 6])  # x軸範囲の設定

# カラーバーの設定
cbar_ax_1 = fig.add_axes([0.7, 0.42, 0.25, 0.02])  # [left, bottom, width, height] # カラーバーの位置を設定
plt.colorbar(pcm, cax=cbar_ax_1, label='振幅', orientation='horizontal', pad=0.5, aspect=40)  # カラーバーを設定


# Continuous Wavelet Transform (CWT) を実施して可視化
scales = np.arange(1, 32)  # スケールの値を設定
cwt_result = cwt(waveform_yesno, morlet, scales)  # CWTを実施
pcm = axes[2].pcolormesh(t_yesno, scales, np.abs(cwt_result), shading='gouraud', cmap='jet')  # CWTの結果をプロット
axes[2].set_xlim([0, 6])  # x軸範囲の設定
axes[2].set_xlabel('時間 [s]')  # x軸のラベルを設定
axes[2].set_ylabel('スケール')  # y軸のラベルを設定

# カラーバーの設定
cbar_ax = fig.add_axes([0.7, 0.12, 0.25, 0.02])  # [left, bottom, width, height]  # カラーバーの位置を設定
plt.colorbar(pcm, cax=cbar_ax, label='ウェーブレット係数', orientation='horizontal')

# plt.colorbar(pcm, ax=axes[2], label='ウェーブレット係数', orientation='horizontal', pad=0.3, shrink=0.4, aspect=40)

# plt.tight_layout()
plt.savefig('7_1_4_stft_cwt_analysis.png', dpi=300)  # 図の保存
plt.show()  # 図の表示
