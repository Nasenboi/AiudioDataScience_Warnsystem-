'''
Title:
    USKSorter.py
Version:
    0

Author(s):
    Christian

Creation Date:
    ?
Update(s):
    Date       | Changes
    24.02.2023 | Added Header

Comment(s):
    This code was used to sort all the audiodata from the Uurban Sound 8k Dataset
    The labeled and sorted Audiodata will be saved into a csv File
    containing following information: 
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

    And always Remember: 0 is false!

Link to the Dataset:
    https://urbansounddataset.weebly.com/urbansound8k.html
'''

import csv
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

#The general Path to the Audiodata and the Destinationpath
path = r"F:\Raw_Audio"
destPath = r"F:\Labeled_Audio"
csvPath = r"F:\labeled_audio_data.csv"

failedFiles = [];

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
    dataFrame  = pd.read_csv(csvPath)
    dfDic = dataFrame.to_dict('list')
    dfKeys = dfDic.keys()
    dicKeys = data_dic.keys()
    for k in dicKeys:
        if k in dicKeys:
            data_dic[k] = dfDic[k]
    del dfDic, dfKeys
else:
    print("Neue Datei wird angelegt.")
    hdr = False

#Lets begin sorting the Google Dataset 
#Done!!!!! (Code ist seperat gespeichert, falls noch änderungen auftrerten sollten)
sourceCSVPath   = r"F:\Raw_Audio\UrbanSound8K\metadata\UrbanSound8K.csv"
sourceAudioPath = r"F:\Raw_Audio\UrbanSound8K\audio\fold"

#Open&format the source CSV to get them data
uskDic = pd.read_csv(sourceCSVPath).to_dict('list')
uskKeys = uskDic.keys()
print(uskKeys)


for f in range(len(uskDic['fsID'])):

    #Categorization
    if uskDic['class'][f] == "air_conditioner":
        mainSound  = "interior"
        threat     = 2
        salience   = 5
        importance = 0
    elif uskDic['class'][f] == "car_horn":
        mainSound  = "car_horn"
        threat     = 7
        salience   = 9
        importance = 9
    elif uskDic['class'][f] == "children_playing":
        mainSound  = "human"
        threat     = 0
        salience   = 5
        importance = 0
    elif uskDic['class'][f] == "dog_bark":
        mainSound  = "animal"
        threat     = 4
        salience   = 5
        importance = 4
    elif uskDic['class'][f] == "drilling":
        mainSound  = "exterior"
        threat     = 0
        salience   = 6
        importance = 0
    elif uskDic['class'][f] == "engine_idling":
        mainSound  = "exterior"
        threat     = 0
        salience   = 4
        importance = 0
    elif uskDic['class'][f] == "gun_shot":
        mainSound  = "gunshot"
        threat     = 9
        salience   = 9
        importance = 9
    elif uskDic['class'][f] == "jackhammer":
        mainSound  = "exterior"
        threat     = 2
        salience   = 8
        importance = 0
    elif uskDic['class'][f] == "siren":
        mainSound  = "siren"
        threat     = 8
        salience   = 9
        importance = 9
    elif uskDic['class'][f] == "street_music":
        mainSound  = "exterior"
        threat     = 0
        salience   = 5
        importance = 0
    else:
        print("Something is not spelled correctly!")
        print(uskDic['class'][f])

    try:
        a = uskDic['slice_file_name'][f]
        fName = a[:-4]
        if fName not in data_dic['filename']:
            fileFolder = sourceAudioPath + str(uskDic['fold'][f])
            filepath = os.path.join(fileFolder, a)
            with wave.open(filepath, mode='rb') as aFile:
                sr = aFile.getframerate()
                length = aFile.getnframes() / sr
                if length <= 0.5:
                    print("Datei:" + fName)
                    print("Datei zu kurz, wird nicht kopiert/beschriftet!")
                else:
                    appendToDatadic(fName, mainSound, length, sr, 7,   1, 0, 0,   threat, salience, importance)
                    sh.copy(filepath, destPath)
                aFile.close()
        else: print("Datei bereits vorhanden")
    except:
        print("Datei:" + fName)
        print("Fold:" + str(uskDic['fold'][f]))
        print("Class:" + uskDic['class'][f])
        print("Failed to append File to Dict")
        failedFiles.append(a)

print("Failed Files:")
print(failedFiles)
print("In prozent:")
percent = len(failedFiles)/len(uskDic['fsID'])
print(percent)
#Overwrite the list of lables
dataFrame = pd.DataFrame.from_dict(data_dic)

dataFrame.to_csv(csvPath, header='column_names')