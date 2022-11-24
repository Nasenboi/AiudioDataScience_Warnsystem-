import os

from AudioDataPackage.AudioPreprocessing.CutAudioData import CutAudioData as cut

path = 'D:\\Final_Audio_Data\\'

def printDirs(filename):
    print(filename)
    try:
        os.chdir(filename)

        new_names = os.listdir()
        for n in new_names:
            f = os.path.join(filename, n)
            printDirs(f)
    except:
        return;

printDirs(path)