
import numpy as np
import librosa
import matplotlib.pyplot as plt
import librosa.display

def SayHi(filename):
    waveform, samplerate = librosa.load(filename)
    waveform, _ = librosa.effects.trim(waveform)

    n = 1024

    fourier = np.abs(librosa.stft(waveform, n))
    fourier_in_dB = librosa.amplitude_to_db(fourier, ref=np.max)
    librosa.display.specshow(fourier_in_dB, sr=samplerate, x_axis='time', y_axis='log')
    plt.show()