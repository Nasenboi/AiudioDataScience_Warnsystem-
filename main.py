import AudioDataPackage.AudioToInputData.AudioToInputData as atid
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

path = r"F:\Labeled_Audio\166101-5-2-4.wav"

sampleRateSpec = 16000

samples, sampleRate = librosa.load(path, sr=sampleRateSpec)

#sampleList = [float(i) for i in range(20)]
#sampleRate = 48000;
#samples = np.array(sampleList)

frames = atid.audioToInputData(samples=samples, sampleRateSample=sampleRate, blockSize=16000, hopSize=8000, specBlockSize=2048, specHopSize=512)
S = np.abs(frames[len(frames)-1])

fig, ax = plt.subplots()
img = librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time', ax=ax, sr = sampleRateSpec)
ax.set_title('Power spectrogram')
fig.colorbar(img, ax=ax, format="%+2.0f dB")

plt.show()