'''
Title:
    main.py
    Later: oldMainCode.py

Version:
    0

Author(s):
    Christian Böndgen

Creation Date:
    ?
Update(s):
    Date       | Changes
    24.02.2023 | Added header

Comment(s):
    In this code I will test the basics of the librosa library ^^

'''


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