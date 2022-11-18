#Hier werde ich nur die Basics von librosa testen ^^
import os
import pandas as pd
import librosa
import librosa.util
#from AudioDataPackage.AudioPreprocessing.CutAudioData import CutAudioData as cut



# 1. Get the file path to an included audio example
path = 'F:\\Raw_Audio\\'

os.chdir(path)

filenames = os.listdir()


data_dic = {
    'filename': [],
    'numSamples': [],
    'sampleRate': []
}

print("Filenames: \n", filenames)

for i in filenames:
    filepath = os.path.join(path, i)
    y, sr = librosa.load(filepath)
    data_dic['filename'].append(i)
    data_dic['numSamples'].append(len(y))
    data_dic['sampleRate'].append(sr)


print("Put in dic")

df = pd.DataFrame(data_dic)

df.to_csv('F:\\audio_data.csv', index=False)

print("made csv :)")