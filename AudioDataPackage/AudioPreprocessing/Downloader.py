'''
Title:
    Downloader.py
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
    With the help of the code written by Aoife McDonagh, this code will download audiofiles from youtube.
    It will take a category from the Youtube AudioSet and create a new Folder to download all the labeled
    audio files from the corresponding Youtube Videos.
    
Link to the Dataset and Github:
    https://research.google.com/youtube8m/index.html
    https://github.com/aoifemcdonagh/audioset-processing
'''

import os
#import AudioDataPackage.AudioSetDownloader

os.chdir(os.getcwd() + "/AudioDataPackage/AudioSetDownloader");
#print(os.getcwd())

destPath = input("Please give me a destination path! \n");
classDownload =  input("And give me a class to download! \n")

print("python3 process.py download -c \"" + classDownload + "\" -d \"" + destPath + "\"");
try:
    os.system("python3 process.py download -c \"" + classDownload + "\" -d \"" + destPath + "\"");
except:
    print("Error!")
