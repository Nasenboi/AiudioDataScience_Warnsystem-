'''
Title:
    AudioSetSorter.py
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
    This code was used to sort all the downloaded audiodata from the Youtube AudioSet
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
        https://research.google.com/youtube8m/index.html
'''

import csv
import os
import wave
import pandas as pd
import shutil as sh

#The general Path to the Audiodata and the Destinationpath
path = r"F:\Raw_Audio"
sourcePath = os.path.join(path, "AudioSet")
os.chdir(sourcePath)
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

#Get the subfolders:
subFolders = os.listdir();
for f in subFolders:
    audioPath = os.path.join(sourcePath, f)
    if os.path.isdir(audioPath):
        print("Ordner:")
        print(f)
        os.chdir(audioPath)
        audioFiles = os.listdir()
        
        #Categorization
        if f == "Bird":
            mainSound  = "animal"
            threat     = 2
            salience   = 5
            importance = 1
        elif f == "Bicycle bell":
            mainSound  = "bicycle_bell"
            threat     = 5
            salience   = 7
            importance = 9
        elif f == "Car":
            mainSound  = "exterior"
            threat     = 2
            salience   = 3
            importance = 3
        elif f == "Emergency Vehicle":
            mainSound  = "emergency_vehicle"
            threat     = 4
            salience   = 9
            importance = 8
        elif f == "Environmental noise":
            mainSound  = "exterior"
            threat     = 0
            salience   = 3
            importance = 0
        elif f == "Explosion":
            mainSound  = "explosion"
            threat     = 9
            salience   = 9
            importance = 9
        elif f == "Fire alarm":
            mainSound  = "siren"
            threat     = 6
            salience   = 9
            importance = 9
        elif f == "Gunshot":
            mainSound  = "gunshot"
            threat     = 9
            salience   = 9
            importance = 9
        elif f == "Screaming":
            mainSound  = "screaming"
            threat     = 5
            salience   = 8
            importance = 5
        elif f == "Siren":
            mainSound  = "siren"
            threat     = 8
            salience   = 9
            importance = 9
        else:
            print("Something is not spelled correctly!")

        
        for a in audioFiles:
            try:
                fName = a[:-4]
                if fName not in data_dic['filename']:
                    filepath = os.path.join(audioPath, a)
                    with wave.open(filepath) as aFile:
                        sr = aFile.getframerate()
                        length = aFile.getnframes() / sr
                        if length <= 0.5:
                            print("Datei:" + fName)
                            print("Datei zu kurz, wird nicht kopiert/beschriftet!")
                        else:
                                appendToDatadic(fName, mainSound, length, sr, 3, 0, 1, 0, threat, salience, importance)
                                sh.copy(filepath, destPath)
            except:
                print("Datei:" + fName)
                print("Failed to append File to Dict")
                failedFiles.append(a)

print("Failed Files:")
print(failedFiles)

#Overwrite the list of lables
dataFrame = pd.DataFrame.from_dict(data_dic)

dataFrame.to_csv(csvPath, header='column_names')