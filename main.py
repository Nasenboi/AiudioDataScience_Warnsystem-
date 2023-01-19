from random import sample
import AudioDataPackage.AudioToInputData.AudioToInputData as atid
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\Chr1s\Documents\Programmierungen\GitHubStuff\AiudioDataScience_Warnsystem-\AudioAugmentation\TrynError\BrumD.wav"

samples, sampleRate = librosa.load(path)

#sampleList = [float(i) for i in range(20)]
#sampleRate = 48000;
#samples = np.array(sampleList)

frames = atid.audioToInputData(samples, sampleRate, sampleRate, int(0.5*sampleRate), 2048, 512)

S = np.abs(frames[len(frames)-1])

fig, ax = plt.subplots()
img = librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time', ax=ax)
ax.set_title('Power spectrogram')
fig.colorbar(img, ax=ax, format="%+2.0f dB")

plt.show()