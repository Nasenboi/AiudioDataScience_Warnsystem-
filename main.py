import AudioDataPackage.AudioToInputData.AudioToInputData as atid
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os

path = r"F:\Labeled_Audio\135526-6-7-0.wav"
specPath = r"F:\Labeled_Specs\135526-6-7-0"

sampleRateSpec = 16000

samples, sampleRate = librosa.load(path, sr=sampleRateSpec)

#sampleList = [float(i) for i in range(20)]
#sampleRate = 48000;
#samples = np.array(sampleList)

if os.path.exists(specPath+".npy"):
    print("lol")
    frames = np.load(specPath+".npy")
else:
    print("make new frames!")
    frames = atid.audioToInputData(samples=samples, sampleRateSample=sampleRate, blockSize=sampleRate*2, hopSize=int(sampleRate*0.9), specBlockSize=2048, specHopSize=256)
    print("Save this shit!")
    np.savez_compressed(specPath, frames)


S = np.abs(frames[0])
fig, ax = plt.subplots()
img = librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time', ax=ax, sr = sampleRateSpec)
ax.set_title('Power spectrogram')
fig.colorbar(img, ax=ax, format="%+2.0f dB")

plt.show()