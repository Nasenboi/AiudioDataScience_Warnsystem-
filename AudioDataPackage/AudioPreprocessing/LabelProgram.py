import os
import pandas as pd
from tkinter import *
from tkinter import messagebox
import sounddevice as sd
import librosa

import threading

#The general Path to the Audiodata and the Destinationpath
path = r"/Users/nickjonas/Desktop/Labeled_Audio/"
audioPath = r"/Users/nickjonas/Desktop/Labeled_Audio/"
csvPath = r"/Users/nickjonas/Desktop/labeled_audio_data.csv"

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

def getCurrentInput (index):
    global data_dic
    global currFilename, currMainSound, currLength, currSampleRate, currQuality, currCut, currMixed, currChecked, currThreat, currSalience, currImportance 
    currFilename = data_dic['filename'][index]
    currMainSound = data_dic['mainSound'][index]
    currLength = data_dic['length'][index]
    currSampleRate = data_dic['sampleRate'][index]
    currQuality = data_dic['quality'][index]
    currCut = data_dic['isCut'][index]
    currMixed = data_dic['isMixed'][index]
    currChecked = data_dic['isChecked'][index]
    currThreat = data_dic['threat'][index]
    currSalience = data_dic['salience'][index]
    currImportance = data_dic['importance'][index]

def reloadValues():
    global threatSlider, salienceSlider, importanceSlider, qualitySlider, fileNameL, mainSounL, mixedBox, cutBox
    threatSlider.set(currThreat)
    salienceSlider.set(currSalience)
    importanceSlider.set(currImportance)
    qualitySlider.set(currQuality)
    fileNameL.config(text = currFilename)
    mainSounL.config(text = currMainSound)
    if currMixed==1: mixedBox.select()
    else: mixedBox.deselect()
    if currCut==1: cutBox.select()
    else: cutBox.deselect()

#Threading function
'''
def printit():
    global stopper, stopper2
    threading.Timer(0.05, printit).start()
    if stopper and stopper2:
        saveAndLoad()
'''

#RIGHT NOW THE CHECKBOXES WONT CHANGE THE CSV FILE, IF ITS NEEDED SOMEWHERE PLS TELL ME
def overwriteOldValues(fileNum):
    global threatSlider, salienceSlider, importanceSlider, qualitySlider, fileNameL, mainSounL, mixedBox, cutBox
    data_dic['quality'][fileNum]     = qualitySlider.get()
    data_dic['isChecked'][fileNum]   += 1
    data_dic['threat'][fileNum]      = threatSlider.get()
    data_dic['salience'][fileNum]    = salienceSlider.get()
    data_dic['importance'][fileNum]  = importanceSlider.get()
    '''
    if mixedBox.get(): data_dic['isMixed'][fileNum] = 1
    else: data_dic['isMixed'][fileNum] = 0
    if cutBox.get(): data_dic['isCut'][fileNum] = 1
    else: data_dic['isCut'][fileNum] = 0
    '''

def getNextUnusedFile():
    global fileNum#, stopper2
    fileNum+=1
    lastIndex = len(data_dic['isChecked'])-1
    while not (data_dic['isChecked'][fileNum] == 0 and data_dic['quality'][fileNum] == 3) and fileNum < lastIndex:
        fileNum+=1

    if fileNum == lastIndex:
        messagebox.askokcancel("Done!", "   You can quit now! \n (The data will be saved!)")
        fileNum = lastIndex-1;
        #stopper2 = False
            

#Button functions
def playAudio():
    global fileNum
    aFile = audioPath + currFilename + ".wav"
    y, sr = librosa.load(aFile)
    sd.play(y, sr)


def saveAndLoad():
    #global stopper
    stopper = False
    overwriteOldValues(fileNum)
    getNextUnusedFile()
    getCurrentInput(fileNum)
    reloadValues()
    #stopper = True


#THE DELETE FUNCTION WONT DELETE THE AUDIO FILE
def deleteAudio():
    aFile = audioPath + data_dic['filename'][fileNum] + ".wav"
    os.remove(aFile);
    del data_dic['filename'][fileNum]
    del data_dic['mainSound'][fileNum]
    del data_dic['length'][fileNum]
    del data_dic['sampleRate'][fileNum]
    del data_dic['quality'][fileNum]
    del data_dic['isCut'][fileNum]
    del data_dic['isMixed'][fileNum]
    del data_dic['isChecked'][fileNum]
    del data_dic['threat'][fileNum]
    del data_dic['salience'][fileNum]
    del data_dic['importance'][fileNum]
    getNextUnusedFile()
    getCurrentInput(fileNum)
    reloadValues()

def closeApp():
    global data_dic
    if messagebox.askokcancel("Quit", "   Do you want to quit? \n (The data will be saved!)"):
        #Overwrite the list of lables
        dataFrame = pd.DataFrame.from_dict(data_dic)

        dataFrame.to_csv(csvPath, header='column_names')
        root.destroy()

#With this Code Ill sort all the Audiodate we got into one Folder and label it
##with a csv File containing following information (Ziemlich selbsterkl�rend lol):
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

#failedFiles = [];

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
    print("Neue Datei wird angelegt.") #This shouldnt occur anymore lol
    hdr = False

#Index to the first unchecked File:
fileNum = 0
getNextUnusedFile()
'''
print("First unchecked File:")
print(data_dic['filename'][fileNum])
'''
getCurrentInput(fileNum)

#Setup the GUI
root = Tk()
root.title("Audio Label Machine")
root.geometry("400x400")
root.resizable(0,0)

root.rowconfigure(0, weight = 2)
for i in range(1,8): root.rowconfigure(i, weight = 1)
root.rowconfigure(8, weight = 2)

titleFont = ('Helvetica', 12, 'bold')
textFont  = ('Helvetica', 10, 'italic')

#Labels
fileLabel       = Label(root, text="Filename:", font = titleFont)
soundLabel      = Label(root, text="MainSound:", font = titleFont)
threatLabel     = Label(root, text = "Threat", font = titleFont)
salienceLabel   = Label(root, text = "Salience", font = titleFont)
importanceLabel = Label(root, text = "Importance", font = titleFont)
mixedLabel      = Label(root, text = "isMixed", font = titleFont)
cutLabel        = Label(root, text = "isCut", font = titleFont)
qualityLabel    = Label(root, text = "Quality", font = titleFont)
fileNameL       = Label(root, text = "XXXXXX", font = textFont)
mainSounL       = Label(root, text = "XXXXXX", font = textFont)

#Slider
threatSlider    = Scale(root, from_=0, to=9, orient='horizontal', length=150)
salienceSlider  = Scale(root, from_=0, to=9, orient='horizontal', length=150)
importanceSlider= Scale(root, from_=0, to=9, orient='horizontal', length=150)
qualitySlider   = Scale(root, from_=0, to=9, orient='horizontal', length=150)

#Buttons
playButton      = Button(root, text = "Play", width=15, command=playAudio)
doneButton      = Button(root, text = "Done", command=saveAndLoad)
deleteButton    = Button(root, text = "Delete", command=deleteAudio)

#Checkboxes
mixedBox        = Checkbutton(root)
cutBox        = Checkbutton(root)

#Sort into Grid:
fileLabel.grid      (row=0, column=0, columnspan=2, padx = 10, pady=10, sticky='n')
soundLabel.grid     (row=0, column=2, columnspan=2, padx = 10, pady=10, sticky='n')

threatLabel.grid    (row=2, column=0, columnspan=2, sticky='s')
salienceLabel.grid  (row=4, column=0, columnspan=2, sticky='s')
importanceLabel.grid(row=6, column=0, columnspan=2, sticky='s')
qualityLabel.grid   (row=6, column=2, columnspan=2, sticky='s')
mixedLabel.grid     (row=2, column=2, columnspan=2, sticky='s')
cutLabel.grid       (row=4, column=2, columnspan=2, sticky='s')

deleteButton.grid   (row=8, column=0, columnspan=1, padx = 5, pady=5, sticky='ew')
playButton.grid     (row=8, column=1, columnspan=2, padx = 5, pady=5, sticky='ew')
doneButton.grid     (row=8, column=3, columnspan=1, padx = 5, pady=5, sticky='ew')

threatSlider.grid    (row=3, column=0, columnspan=2, padx = 5, pady=5, sticky='n')
salienceSlider.grid  (row=5, column=0, columnspan=2, padx = 5, pady=5, sticky='n')
importanceSlider.grid(row=7, column=0, columnspan=2, padx = 5, pady=5, sticky='n')
qualitySlider.grid   (row=7, column=2, columnspan=2, padx = 5, pady=5, sticky='n')

mixedBox.grid        (row=3, column=2, columnspan=2, sticky='n')
cutBox.grid          (row=5, column=2, columnspan=2, sticky='n')

fileNameL.grid      (row=0, column=0, columnspan=2, padx = 5, pady=5, sticky='s')
mainSounL.grid      (row=0, column=2, columnspan=2, padx = 5, pady=5, sticky='s')

reloadValues()
root.protocol("WM_DELETE_WINDOW", closeApp)
#stopper = True
#stopper2 = True
#printit()
root.mainloop()

'''
#Overwrite the list of lables
dataFrame = pd.DataFrame.from_dict(data_dic)

dataFrame.to_csv(csvPath, header='column_names')
'''


