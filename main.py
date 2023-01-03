import os
import wave
import pandas as pd
import shutil as sh


#Some nice Functions
def appendToDatadic (fName, ms, length, sr, q, ic, im, ich, the, sal, imp):
    global data_dic
    data_dic['filename'].append(fName)
    data_dic['mainSound'].append(ms)
    data_dic['length'].append(length)
    data_dic['sampleRate'].append(sr)
    data_dic['quality'].append(q)
    data_dic['isCut'].append(ic)
    data_dic['isMixed'].append(im)
    data_dic['isChecked'].append(ich)
    data_dic['threat'].append(the)
    data_dic['salience'].append(sal)
    data_dic['importance'].append(imp)


#With this Code Ill sort all the Audiodate we got into one Folder and label it
##with a csv File containing following information (Ziemlich selbsterklärend lol):
'''   
    'filename':     Name of the File (without .wav)
    'mainSound':    The most important sound of the audiofile
    'length':       Length of the File in s
    'sampleRate':   Samplerate in Hz
    'quality':      Rated Quality of the File (Noise, Loundness, etc.)
    'isCut':        Is the File part of something bigger
    'is Mixed':     Does the Audio Signal contain multiple Audiosources
    'isChecked':    How many Times was the File quality Checked
    'threat':       Threat level of main Audio source (0-9)
    'salience':     Salience of main Audio source (0-9)
    'importance':   Importance of main Audio source (0-9)
'''
#And always Remember: 0 is false!


#The general Path to the Audiodata and the Destinationpath
path = r"F:\Raw_Audio"
destPath = r"F:\Labeled_Audio"
csvPath = r"F:\labeled_audio_data.csv"

#Python dictionary containing all the needed data for the labeling
data_dic = {
    'filename': [],
    'mainSound': [],
    'length': [],
    'sampleRate': [],
    'quality': [],
    'isCut': [],
    'isMixed': [],
    'isChecked': [],
    'threat': [],
    'salience': [],
    'importance': []
}

#Try to open the CSV to see if there is already Data in there
if os.path.exists(csvPath):
    print("Label Datei existiert, wird erweitert...")
    hdr = True
else:
    print("Neue Datei wird angelegt.")
    hdr = False

#Lets begin sorting the Google Dataset
sourcePath = os.path.join(path, "AudioSet")
os.chdir(sourcePath)

#Get the subfolders:
subFolders = os.listdir();
for f in subFolders:
    audioPath = os.path.join(sourcePath, f)
    if os.path.isdir(audioPath) and f == 'Bird':
        print("Ordner:")
        print(f)
        os.chdir(audioPath)
        audioFiles = os.listdir()
        for a in audioFiles:
            if a in data_dic['filename']:
                print("Datei ist bereits beschriftet")
            else:
                filepath = os.path.join(audioPath, a)
                print(a[0:-4])
                with wave.open(filepath) as aFile:
                    sr = aFile.getframerate()
                    length = aFile.getnframes() / sr
                    appendToDatadic(a[0:-4], f, length, sr, 3, 0, 1, 0, 0, 3, 1)
                    sh.copy(filepath, destPath)

#Overwrite the list of lables
dataFrame = pd.DataFrame.from_dict(data_dic)
if hdr:
    dataFrame.to_csv(r'F:\labled_audio_data.csv',mode = 'a',header = False)
else:
    dataFrame.to_csv(r'F:\labled_audio_data.csv', header='column_names')