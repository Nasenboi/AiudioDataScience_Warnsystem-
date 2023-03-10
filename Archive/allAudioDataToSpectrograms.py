'''
Title:
    allAudioDataToSpectrograms
Version:
    0

Author(s):
    Christian Böndgen

Creation Date:
    ?
Update(s):
    Date       | Changes
    09.03.23   | Moved file to the archive and added header

Comment(s):
    This Code turned all the audio data we got into
    Spectrograms.
    The form of said spectrograms looks like this:
    First the audio file is cut into smaller segments with:
    16kHz samplerate, 2s length and a 900ms hopsize
    Then these audio snippets are turned into a log spectrogram with:
    2048 bins and a 256 sample hopsize
'''

import AudioDataPackage.AudioToInputData.AudioToInputData as atid
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os

audioPath = r"F:\Labeled_Audio"
specPath = r"F:\Labeled_Specs"

sampleRateSpec = 16000

allAudioFiles = os.listdir(audioPath)

fileLength = len(allAudioFiles)
counter = 0

for audioFile in allAudioFiles:
    samples, sampleRate = librosa.load(os.path.join(audioPath, audioFile), sr=sampleRateSpec)
    #print("Audiofile:", audioFile)
    specSavePath = os.path.join(specPath, audioFile[:-4])
    #print(specSavePath+".npz")
    if os.path.exists(specSavePath+".npz"):
        #print("File already exists!")
        try:
            frames = np.load(specSavePath+".npz")
            frames = frames[frames.files[0]]
        except:
            frames = atid.audioToInputData(samples=samples, sampleRateSample=sampleRate, blockSize=sampleRate*2, hopSize=int(sampleRate*0.9), specBlockSize=2048, specHopSize=256)
            np.savez_compressed(specSavePath, data = frames, allow_pickle=False)
    else:
        #print("Build the spectrogram!")
        frames = atid.audioToInputData(samples=samples, sampleRateSample=sampleRate, blockSize=sampleRate*2, hopSize=int(sampleRate*0.9), specBlockSize=2048, specHopSize=256)
        np.savez_compressed(specSavePath, data = frames)
    counter += 1
    if counter%10==0:
        print("(", counter, "/", fileLength, ") Files done", sep="")
        print("-"*80)

'''
fig, ax = plt.subplots()
img = librosa.display.specshow(frames[0], x_axis='time', y_axis='linear', ax=ax)
ax.set(title="Spectrogram")
fig.colorbar(img, ax=ax, format="%+2.f dB")

plt.show()
'''

print("All spectrograms are made :D")