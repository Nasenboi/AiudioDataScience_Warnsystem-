#title:
#    spectrogramCheck
#version:
#    0
#
#author(s):
#    Christian Böndgen
#
#creation date:
#    09.03.23
#update(s):
#    date       | changes
#    09.03.23   | created the file and wrote the first code

#comment(s):
#    this program checks to see if all spectrograms were made.
#    in a future version this code mabe could show some of the
#    spectrograms to verify if they look right.

import pandas as pd
import numpy as np
import os

csvPath = r"F:\labeled_audio_data.csv"
specPath = r"F:\Labeled_Specs"

print("Are all Spectrograms done?")

dataFrame = pd.read_csv(csvPath)
dictionary = dataFrame.to_dict()
classifiedAudio = list(dictionary['filename'].values())

allSpectrograms = os.listdir(specPath)

lostFiles = []

for audioObject in classifiedAudio:
    if audioObject+".npz" not in allSpectrograms:
        lostFiles.append(audioObject)

if len(lostFiles) == 0:
    print("All good, all Specs are there!")
else:
    print(len(lostFiles), " files are missing!")
    print(lostFiles)