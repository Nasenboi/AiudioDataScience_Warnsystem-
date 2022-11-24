#Hier werde ich nur die Basics von librosa testen ^^
import os
import pandas as pd
import librosa
import librosa.util


if __name__ == "__main__":
    # 1. Get the file path to an included audio example
    path = 'D:\\Raw_Audio\\'

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
        y, sr = librosa.load(filepath) #, sr = 44100
        librosa.frames
        data_dic['filename'].append(i)
        data_dic['numSamples'].append(len(y))
        data_dic['sampleRate'].append(sr)


    print("Put in dic")

    df = pd.DataFrame(data_dic)

    df.to_csv('D:\\audio_data.csv', index=False)

    print("made csv :)")
