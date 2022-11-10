#Hier werde ich nur die Basics von librosa testen ^^
import os
import numpy as np
import librosa
import matplotlib.pyplot as plt
import librosa.display

# 1. Get the file path to an included audio example
filename = 'AudioData/bruh.wav'

waveform, samplerate = librosa.load(filename)
waveform, _ = librosa.effects.trim(waveform)

n = 1024

fourier = np.abs(librosa.stft(waveform, n))
fourier_in_dB = librosa.amplitude_to_db(fourier, ref=np.max)
librosa.display.specshow(fourier_in_dB, sr=samplerate, x_axis='time', y_axis='log')
plt.show()