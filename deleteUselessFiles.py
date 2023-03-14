'''
Title:
    deleteUselessFiles.py
Version:
    0

Author(s):
    Christian Boendgen

Creation Date:
    13.03.2023
Update(s):
    Date       | Changes
    13.03.2023 | Created the Code

Comment(s):
    This code is going to delete all the unnecessary audiofiles
    from the csv. This is done to create more variance in the training
    dataset that the Neural Network is less likely to just use the average
    value instead of a real guess.
    The files to delete are:
    6/7 animal   | keep every 7th file  (dont delete the angry dog noises!)
    1/2 interior | keep every 2nd file
    1/2 Natural  | keep every 2nd file
    2/3 human    | keep every 3rd file

    later:
    6/7 exterior | keep every 7th file
    1/2 siren    | keep every 2nd file

    The above solution did not really work.
    The new plan is to only use audio files that change the average values of
    the three categorys (threat, salience and importance)

'''

import pandas as pd
from statistics import mean
from random import sample, random
#import os

csvPath = r"F:\labeled_audio_data_old.csv"
newCsvPath = r"F:\labeled_audio_data.csv"

dataFrame = pd.read_csv(csvPath)
dataDict = dataFrame.to_dict()

dataDictNew = {
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

numFiles = len(dataDict[list(dataDict.keys())[0]].values())

fileNum = 0

def appendToDict():
    #global fileNum, dataDict, dataDictNew
    dataDictNew['filename']  .append(dataDict['filename'][fileNum])
    dataDictNew['mainSound'] .append(dataDict['mainSound'][fileNum])
    dataDictNew['length']    .append(dataDict['length'][fileNum])
    dataDictNew['sampleRate'].append(dataDict['sampleRate'][fileNum])
    dataDictNew['quality']   .append(dataDict['quality'][fileNum])
    dataDictNew['isCut']     .append(dataDict['isCut'][fileNum])
    dataDictNew['isMixed']   .append(dataDict['isMixed'][fileNum])
    dataDictNew['isChecked'] .append(dataDict['isChecked'][fileNum])
    dataDictNew['threat']    .append(dataDict['threat'][fileNum])
    dataDictNew['salience']  .append(dataDict['salience'][fileNum])
    dataDictNew['importance'].append(dataDict['importance'][fileNum])


avgThreat = 0
avgSalience = 0
avgImportance = 0

space     = 2
randRange = 3 # A 1 means values from -0.5 to 0.5

def isNear(value, compare):
    if (value > (compare + space)) or (value < (compare-space)):
        return True
    else:
        return False

def calcAverage(value, average, size):
    return (((size-1)*average + value)/size)

newNumFiles = 0

def randomVal():
    return (random() - 0.5) * randRange


cats = [["exterior",    8], ["animal",            3],
        ["siren",       0], ["emergency_vehicle", 0],
        ["gunshot",    99], ["screaming",        99],
        ["explosion",  99], ["bicycle_bell",      0],
        ["interior",    2], ["natural",           1],
        ["human",      99], ["fireworks",        99],
        ["clock_alarm", 0], ["car_horn",         99],
        ["fire",       99], ["crying_baby",      99]]

counters = [0 for i in range(len(cats))]

#iterate though all files:
for fileNum in sample(range(numFiles), numFiles):
    for i in range(len(cats)):
        if dataDict['mainSound'][fileNum] == cats[i][0]:
            if counters[i] > cats[i][1] and cats[i][1] != 99:
                appendToDict()
                newNumFiles += 1
                counters[i]  = 0
            counters[i]  += 1
            break

print("Old size :", numFiles)
print("New size :", newNumFiles)
print("Del Files:", numFiles-newNumFiles)

#Save the new dict
df = pd.DataFrame.from_dict(dataDictNew)

df.to_csv(newCsvPath, header='column_names')



'''
This was an old try but it didnt work

animalCounter   = 0
interiorCounter = 0
naturalCounter  = 0
humanCounter    = 0
exteriorCounter = 0
sirenCounter    = 0


    if dataDict['mainSound'][fileNum] == "animal":
        if dataDict['threat'][fileNum] > 4:
            appendToDict()
        else:
            if animalCounter > 6:
                appendToDict()
                animalCounter = 0
        animalCounter += 1
    elif dataDict['mainSound'][fileNum] == "interior":
        if dataDict['threat'][fileNum] > 3:
            appendToDict()
        else:
            if interiorCounter > 1:
                appendToDict()
                interiorCounter = 0
        interiorCounter += 1
    elif dataDict['mainSound'][fileNum] == "exterior":
        if dataDict['threat'][fileNum] > 3:
            appendToDict()
        else:
            if exteriorCounter > 6:
                appendToDict()
                exteriorCounter = 0
        exteriorCounter += 1
    elif dataDict['mainSound'][fileNum] == "natural":
        if naturalCounter > 1:
            appendToDict()
            naturalCounter = 0
        naturalCounter += 1
    elif dataDict['mainSound'][fileNum] == "human":
        if humanCounter > 2:
            appendToDict()
            humanCounter = 0
        humanCounter += 1
    elif dataDict['mainSound'][fileNum] == "siren":
        if sirenCounter > 2:
            appendToDict()
            sirenCounter = 0
        sirenCounter += 1
    else:
        appendToDict()
'''


'''
    Another epic failed attempt

    threat     = dataDict['threat'][fileNum]      + randomVal()
    salience   = dataDict['salience'][fileNum]    + randomVal()
    importance = dataDict['importance'][fileNum]  + randomVal()
    if isNear(threat, avgThreat) and isNear(salience, avgSalience) and isNear(importance, avgImportance):
        appendToDict()
        newNumFiles += 1
        avgThreat     = calcAverage(threat, avgThreat, newNumFiles)
        avgSalience   = calcAverage(salience, avgSalience, newNumFiles)
        avgImportance = calcAverage(importance, avgImportance, newNumFiles)



'''