'''
Title:

Version:
    0

Author(s):
    

Creation Date:
    
Update(s):
    Date       | Changes
    

Comment(s):
    

'''

import audioop
import os
import pandas as pd

csvPath = r"F:/labeled_audio_data.csv"
audioPath = r"F:/Labeled_Audio"

allLabeledAudios = os.listdir(audioPath)

dataFrame = pd.read_csv(csvPath)
dictionary = dataFrame.to_dict()
classifiedAudio = list(dictionary['filename'].values())

print("Deleted Audiofiles:", len(allLabeledAudios) - len(classifiedAudio))

deletedAudioFiles = []

for audio in allLabeledAudios:
    if audio[:-4] not in classifiedAudio:
        deletedAudioFiles.append(audio)
        #This will delete all the bad audiodata!
        #os.remove(os.path.join(audioPath, audio))