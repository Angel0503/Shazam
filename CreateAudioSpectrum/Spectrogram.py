from scipy.io import wavfile
import numpy as np
import os
from scipy import signal
from scipy.signal.windows import blackman
import matplotlib.pyplot as plt

current_dir = os.getcwd()
AudioName = f"{current_dir}\\CreateAudioSpectrum\\AudioFile\\new-edm-music-beet-mr-sandeep-rock-141616.wav"
fs, Audiodata = wavfile.read(AudioName)

# If stereo, convert to mono
if len(Audiodata.shape) > 1:
    Audiodata = np.mean(Audiodata, axis=1)

N = min(512, len(Audiodata))  # Ensure N is not larger than the input signal
window = blackman(N)  # Use the new import path for blackman window

f, t, Sxx = signal.spectrogram(Audiodata, fs, window=window, nfft=N)

plt.pcolormesh(t, f, 10 * np.log10(Sxx))
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()