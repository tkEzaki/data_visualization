import torchaudio
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, fftfreq, ifft
from scipy.signal import stft, cwt, morlet, ricker
import japanize_matplotlib

plt.rcParams['font.size'] = 16

# Function to compute Fourier approximation


def fourier_approximation(fft_values, n_terms, N, t):
    fft_approx = np.zeros_like(fft_values)
    # Keep only the first few terms
    fft_approx[:n_terms + 1] = fft_values[:n_terms + 1]
    fft_approx[-n_terms:] = fft_values[-n_terms:]
    # Compute the inverse FFT to get the time domain signal
    signal_approx = ifft(fft_approx).real
    return signal_approx


# Set the audio backend
torchaudio.set_audio_backend("soundfile")

# YESNOデータセットをダウンロードして読み込む
dataset = torchaudio.datasets.YESNO('.', download=False)
waveform_yesno, sample_rate, *_ = dataset[0]
waveform_yesno = waveform_yesno.numpy().flatten()
t_yesno = np.linspace(0, len(waveform_yesno) / sample_rate, len(waveform_yesno), endpoint=False)

# Parameters for synthetic data
sampling_rate = 44100
duration = 1.0
N = int(sampling_rate * duration)
t = np.linspace(0, duration, N, endpoint=False)

# Generate three sine waves
freqs_sine = [2, 10, 20]
amplitudes_sine = [1, 0.5, 0.2]
sine_wave = np.sum([amplitudes_sine[i] * np.sin(2 * np.pi * freqs_sine[i] * t) for i in range(len(freqs_sine))], axis=0)

# Generate a triangular wave
freq_triangle = 2
triangle_wave = 0.5 * (1 + np.sign(np.sin(2 * np.pi * freq_triangle * t)))

# List of data for plotting
data_list = [sine_wave, triangle_wave, waveform_yesno]
titles = ['Three Sine Waves', 'Triangle Wave', 'YESNO Sample']
time_arrays = [t, t, t_yesno]

# Create subplots
fig, axes = plt.subplots(len(data_list), 2, figsize=(10, 12))

for i, (data, title, time_array) in enumerate(zip(data_list, titles, time_arrays)):
    # Time-domain plot
    axes[i, 0].plot(time_array, data, label='Original', color="k", alpha=0.6)

    # Add Fourier approximations for sine and triangle waves
    if title == 'Three Sine Waves':
        for n in [2, 10]:
            approx = fourier_approximation(fft(data), n, N, t)
            axes[i, 0].plot(time_array, approx, label=f'{n}-term Fourier Approx', linestyle='--', alpha=0.6)
    elif title == 'Triangle Wave':
        for n in [5, 10, 50]:
            approx = fourier_approximation(fft(data), n, N, t)
            axes[i, 0].plot(time_array, approx, label=f'{n}-term Fourier Approx', linestyle='--', alpha=0.6)

    # axes[i, 0].set_title(f'Time Domain: {title}')
    axes[i, 0].set_xlabel('時間 [s]')
    axes[i, 0].set_ylabel('')
    # axes[i, 0].legend()

    # Frequency-domain plot (Power Spectrum)
    N_fft = len(data)
    freq_values = fftfreq(N_fft, 1 / sampling_rate)
    fft_values = fft(data)
    magnitude = np.abs(fft_values) / N  # Normalize
    # magnitude = np.abs(fft_values)

    # Only plot the positive frequencies
    positive_freq_idxs = np.where(freq_values > 0)
    axes[i, 1].plot(freq_values[positive_freq_idxs], magnitude[positive_freq_idxs], color="k", alpha=0.6)
    # axes[i, 1].set_title(f'Power Spectrum: {title}')
    axes[i, 1].set_xlabel('周波数 [Hz]')
    axes[i, 1].set_ylabel('振幅')

    # Extend frequency range up to 5000 Hz only for YESNO sample
    if title == 'YESNO Sample':
        axes[i, 1].set_xlim([0, 5000])
    else:
        axes[i, 1].set_xlim([0, 50])


plt.tight_layout()
plt.savefig('7_1_3_fourier_analysis.png', dpi=300)
plt.savefig('7_1_3_fourier_analysis.svg', dpi=300)
plt.show()


plt.rcParams['font.size'] = 12
# Additional plot for STFT and Wavelet Transform of YESNO Sample
fig, axes = plt.subplots(3, 1, figsize=(8, 6))
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9, wspace=0.0, hspace=1.5)

# Time-domain plot for YESNO sample
axes[0].plot(t_yesno, waveform_yesno, label='Original', color="k", alpha=0.6)
axes[0].set_xlabel('時間 [s]')
axes[0].set_ylabel('')
axes[0].set_xlim([0, 6])

# Perform Short-Time Fourier Transform (STFT) and visualize
frequencies, time_stft, Zxx = stft(waveform_yesno, fs=sample_rate, nperseg=128)

# Frequency-domain plot (STFT) for YESNO sample
pcm = axes[1].pcolormesh(time_stft, frequencies, np.abs(Zxx), shading='gouraud', cmap='jet')
axes[1].set_xlabel('時間 [s]')
axes[1].set_ylabel('周波数 [Hz]')
axes[1].set_xlim([0, 6])
cbar_ax_1 = fig.add_axes([0.7, 0.42, 0.25, 0.02])  # [left, bottom, width, height]
plt.colorbar(pcm, cax=cbar_ax_1, label='振幅', orientation='horizontal', pad=0.5, aspect=40)


scales = np.arange(1, 32)
cwt_result = cwt(waveform_yesno, morlet, scales)  # Using the new scale values
pcm = axes[2].pcolormesh(t_yesno, scales, np.abs(cwt_result), shading='gouraud', cmap='jet')
axes[2].set_xlim([0, 6])
# pcm = axes[2].imshow(np.abs(cwt_result), aspect='auto')#, extent=[0, 6, scales[0], scales[-1]], cmap='jet') #, interpolation='bilinear')
axes[2].set_xlabel('時間 [s]')
axes[2].set_ylabel('スケール')

# Create an 'Axes' for the colorbar
cbar_ax = fig.add_axes([0.7, 0.12, 0.25, 0.02])  # [left, bottom, width, height]
plt.colorbar(pcm, cax=cbar_ax, label='ウェーブレット係数', orientation='horizontal')

# plt.colorbar(pcm, ax=axes[2], label='ウェーブレット係数', orientation='horizontal', pad=0.3, shrink=0.4, aspect=40)

# plt.tight_layout()
# plt.savefig('7_1_4_stft_cwt_analysis.png', dpi=300)

# Clear contents of axes[1] and axes[2]
axes[1].cla()
axes[1].set_xlabel('時間 [s]')
axes[1].set_ylabel('周波数 [Hz]')
axes[1].set_xlim([0, 6])
axes[1].set_ylim([0, 4000])

axes[2].cla()
axes[2].set_xlabel('時間 [s]')
axes[2].set_ylabel('スケール')
axes[2].set_xlim([0, 6])
axes[2].set_ylim([1, 31])


plt.savefig('7_1_4_stft_cwt_analysis.svg', dpi=300)
plt.show()
